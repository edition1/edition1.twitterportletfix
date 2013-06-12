import logging
import socket
import twitter

from collective.twitterportlet.portlet import DEFAULT_TIMEOUT
from collective.twitterportlet.portlet import Renderer as OriginalRenderer
from collective.twitterportlet.portlet import TWITTER_TIMEOUT
from collective.twitterportlet.portlet import _render_cachekey
from plone.memoize import ram
from plone.registry.interfaces import IRegistry
from urllib2 import URLError
from zope.component import getUtility

from edition1.twitterportletfix.interfaces import ITwitterSettings


logger = logging.getLogger('edition1.twitterportletfix')


class Renderer(OriginalRenderer):
    """Override the render to use OAuth."""

    @ram.cache(_render_cachekey)
    def get_tweets(self):
        username = self.data.username
        limit = self.data.count
        include_retweets = self.data.include_retweets
        # Ugly workaround for a missing timeout handling in the
        # python-twitter library, see:
        # http://code.google.com/p/python-twitter/issues/detail?id=92
        timeout = socket.getdefaulttimeout()
        # Try to deal with multi-threading in some basic crude way.
        # If we get our own "marker timeout", this code is called in a
        # different thread before the timeout could be reset again. Fall
        # back on the global timeout at import time. Using a thread lock
        # won't help, as other code in other threads could change the same
        # global value
        if timeout == TWITTER_TIMEOUT:
            timeout = DEFAULT_TIMEOUT
            logger.warning('conflict in socket default timeout, resetting '
                           'default timeout to %s' % DEFAULT_TIMEOUT)
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ITwitterSettings)
        try:
            socket.setdefaulttimeout(TWITTER_TIMEOUT)
            twapi = twitter.Api(settings.consumer_key,
                                settings.consumer_secret,
                                settings.access_token,
                                settings.access_token_secret)
            try:
                tweets = twapi.GetUserTimeline(
                    username, count=limit, include_rts=include_retweets)
            except (URLError, twitter.TwitterError, socket.timeout):
                logger.info('Error while fetching data.', exc_info=True)
                tweets = None
        finally:
            socket.setdefaulttimeout(timeout)
        return tweets
