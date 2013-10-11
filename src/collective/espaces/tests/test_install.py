import unittest2 as unittest

from AccessControl import getSecurityManager
from Products.CMFCore.utils import getToolByName
from plone.app.testing import TEST_USER_NAME, TEST_USER_ID, setRoles, login, logout

from collective.espaces.testing import \
    COLLECTIVE_ESPACES_INTEGRATION_TESTING


class TestInstall(unittest.TestCase):

    layer = COLLECTIVE_ESPACES_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product
            installed
        """
        pid = 'collective.espaces'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')


    def test_permissions(self):
        setRoles(self.portal, TEST_USER_ID, ['Site Administrator'])
        login(self.portal, TEST_USER_NAME)
        self.portal.invokeFactory('collective.spaces.space', 'space')
        self.portal.space.manage_addLocalRoles(TEST_USER_ID, ['Editor'])
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        login(self.portal, TEST_USER_NAME)
        sm = getSecurityManager()
        self.assertTrue(
            sm.checkPermission('Portlets: Manage portlets',
                               self.portal.space))
        self.assertTrue(
            sm.checkPermission('plone.portlet.static: Add static portlet',
                               self.portal.space))

    def test_sharing_view(self):
        from collective.espaces.browser.sharing import SharingView

        setRoles(self.portal, TEST_USER_ID, ['Site Administrator'])
        login(self.portal, TEST_USER_NAME)
        self.portal.invokeFactory('collective.spaces.space', 'space')
        login(self.portal, TEST_USER_NAME)
        self.portal.space.invokeFactory('Folder', 'sub_folder')
        context = self.portal.space.sub_folder

        #Should not be able to edit inherited settings on Space content
        view = SharingView(context, self.portal.REQUEST)
        self.assertFalse(view.can_edit_inherit())

        #Should be able to edit normally
        view = SharingView(self.portal, self.portal.REQUEST)
        self.assertTrue(view.can_edit_inherit())

    def test_create_space_view(self):
        from AccessControl import Unauthorized

        setRoles(self.portal, TEST_USER_ID, ['Authenticated'])
        login(self.portal, TEST_USER_NAME)
        self.assertRaises(
            Unauthorized,
            self.portal.restrictedTraverse,
            ('@@create-space',))

        setRoles(self.portal, TEST_USER_ID, ['Shibboleth Authenticated'])
        login(self.portal, TEST_USER_NAME)
        view = self.portal.restrictedTraverse('@@create-space')
        self.assertEqual(view.url(), 'http://nohost/plone/create-space')

