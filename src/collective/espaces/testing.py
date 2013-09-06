from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CollectiveespacesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.espaces
        xmlconfig.file(
            'configure.zcml',
            collective.espaces,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.espaces:default')

COLLECTIVE_ESPACES_FIXTURE = CollectiveespacesLayer()
COLLECTIVE_ESPACES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_ESPACES_FIXTURE,),
    name="CollectiveespacesLayer:Integration"
)
COLLECTIVE_ESPACES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_ESPACES_FIXTURE, z2.ZSERVER_FIXTURE),
    name="CollectiveespacesLayer:Functional"
)
