.. contents::

Introduction
============

This package is intended to be a quick fix for the problem that the
latest release of `collective.twitterportlet`_ (version 0.10) does not
work with the Twitter API v1.1.

.. _`collective.twitterportlet`: https://pypi.python.org/pypi/collective.twitterportlet

By installing this package in your Plone site, you get an additional
configlet. In this configlet you can (or rather: must) configure your
Twitter tokens. This package then overrides the ``Render`` method of
the Twitter portlet to extract these tokens and use them for the
Twitter API calls.


Usage
=====

TODO
