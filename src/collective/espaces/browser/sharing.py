from plone.app.workflow.browser.sharing import SharingView as OriginalSharingView, AUTH_GROUP
from plone.memoize.instance import memoize
from plone.app.layout.navigation.root import getNavigationRootObject
from collective.spaces.interfaces import ISpace

class SharingView(OriginalSharingView):

    STICKY = ()

    @memoize
    def existing_role_settings(self):
        """ Hide the 'Logged in users' entry from the Sharing page.
        """
        info = super(SharingView, self).existing_role_settings()
        result =  filter(lambda v: v['id'] != AUTH_GROUP, info)
        return result

    def can_edit_inherit(self):
        """ Allow inherited roles on everything except content in Spaces.
        """
        navigation_root = getNavigationRootObject(self.context, None)
        return not ISpace.providedBy(navigation_root)
