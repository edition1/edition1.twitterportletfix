from plone.app.registry.browser import controlpanel

from edition1.twitterportletfix.interfaces import ITwitterSettings
from edition1.twitterportletfix import MessageFactory as _


class TwitterSettingsEditForm(controlpanel.RegistryEditForm):

    schema = ITwitterSettings
    label = _(u'Twitter settings')
    description = _(u'help_twitter_setings',
                    default='Lets you configure your Twitter settings.')


class TwitterControlPanel(controlpanel.ControlPanelFormWrapper):
    """Twitter control panel view"""

    form = TwitterSettingsEditForm
