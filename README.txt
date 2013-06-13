.. contents::

Introduction
============

This package is intended to be a quick (and slightly dirty) fix for
the problem that the latest release of `collective.twitterportlet`_
(version 0.10) does not work with the Twitter API v1.1.

.. _`collective.twitterportlet`: https://pypi.python.org/pypi/collective.twitterportlet

By installing this package in your Plone site, you get an additional
configlet. In this configlet you can (or rather: must) configure your
Twitter tokens. This package then overrides the renderer of
the Twitter portlet to use these tokens for the Twitter API calls.


Installation
============

To enable this package in a buildout based instance, add the following
to your buildout configuration::

    [instance]
    ...
    eggs =
        ...
        edition1.twitterportletfix

After you have rerun the ``bin/buildout`` and restarted your instance,
this product should be available for installation.

1. Go to the "Site Setup" page in your Plone site.
2. Click on the "Add-ons" link.
3. Install the "Twitter portlet API v1.1 fix" product.


Usage
=====

Once installed, you need to configure the keys.

First you'll have to create a Twitter application.

1. Go to https://dev.twitter.com/ and log in with your Twitter account.
2. Go to the `My applications`_ page.
3. Create a new application.
4. Immediately create your access token (so your application can
   access your account).
5. Go to the "settings" tab and keep this window open because we'll be
   copying information to your Plone site in a minute.

Now go back to your Plone site.

1. Go to the "Site Setup" page in your Plone site.
2. Click on the "Twitter settings" link.
3. Copy all the required values from the Twitter application page.

And you are done. That is, assuming you already had a Twitter portlet
in your site, it should now work again.

.. _`My applications`: https://dev.twitter.com/apps


Caveats
=======

In the Twitter portlet from collective.twitterportlet, you can
configure from which user the tweets should be shown. Although this
username is still used for the link to the Twitter profile page, it is
**not** used to determine who's tweets to show. This is determined
solely by the access token (and secret) that you configured.

Furthermore, you can only configure **one** account with this fix. So
if you have more than one Twitter portlets and want to show tweets
from different accounts, you are out of luck.


Disclaimer
==========

This package has only been tested on Plone 4.1.6 (Python 2.6) and
Plone 4.3 (Python 2.7) since those were the only version we needed this
fix for. However, it probably also works on other versions of Plone.
