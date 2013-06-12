from zope.i18nmessageid import MessageFactory as ZMF

MessageFactory = ZMF('edition1.twitterportletfix')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
