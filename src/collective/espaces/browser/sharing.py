from AccessControl import getSecurityManager
from Products.CMFCore.permissions import ManagePortal
from plone.app.workflow.browser.sharing import SharingView as OriginalSharingView, AUTH_GROUP
from plone.memoize.instance import memoize
#from plone.app.layout.navigation.root import getNavigationRootObject
#from collective.spaces.interfaces import ISpace

class SharingView(OriginalSharingView):

    @property
    def STICKY(self):
        sticky = ()
        security = getSecurityManager()
        if security.checkPermission(ManagePortal, self.context):
           sticky = (AUTH_GROUP,)
        return sticky

    @memoize
    def existing_role_settings(self):
        """ Hide the 'Logged in users' entry from the Sharing page.
        """
        info = super(SharingView, self).existing_role_settings()
        security = getSecurityManager()
        if security.checkPermission(ManagePortal, self.context):
            return info
        else:
            return filter(lambda v: v['id'] != AUTH_GROUP, info)

#    def can_edit_inherit(self):
#        """ Allow inherited roles on everything except content in Spaces.
#        """
#        navigation_root = getNavigationRootObject(self.context, None)
#        return not ISpace.providedBy(navigation_root)
