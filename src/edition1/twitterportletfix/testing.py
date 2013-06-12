from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class Edition1TwitterportletfixLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import edition1.twitterportletfix
        xmlconfig.file(
            'configure.zcml',
            edition1.twitterportletfix,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edition1.twitterportletfix:default')

EDITION1_TWITTERPORTLETFIX_FIXTURE = Edition1TwitterportletfixLayer()
EDITION1_TWITTERPORTLETFIX_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDITION1_TWITTERPORTLETFIX_FIXTURE,),
    name="Edition1TwitterportletfixLayer:Integration"
)
EDITION1_TWITTERPORTLETFIX_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDITION1_TWITTERPORTLETFIX_FIXTURE, z2.ZSERVER_FIXTURE),
    name="Edition1TwitterportletfixLayer:Functional"
)
