from zope.interface import Interface
from zope import schema

from edition1.twitterportletfix import MessageFactory as _


class ITwitterPortletFixLayer(Interface):
    """Marker interface that defines a Zope 3 browser layer."""


class ITwitterSettings(Interface):
    """Twitter settings."""

    consumer_key = schema.TextLine(
        title=_(u'label_consumer_key', default='Consumer key'),
    )

    consumer_secret = schema.TextLine(
        title=_(u'label_consumer_secret', default='Consumer secret')
    )

    access_token = schema.TextLine(
        title=_(u'label_access_token', default='Access token')
    )

    access_token_secret = schema.TextLine(
        title=_(u'label_access_token_secret', default='Access token secret')
    )
