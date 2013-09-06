from plone.app.workflow.browser.sharing import SharingView as OriginalSharingView, AUTH_GROUP
from plone.memoize.instance import memoize

class SharingView(OriginalSharingView):

    STICKY = ()

    @memoize
    def existing_role_settings(self):
        """ Hide the 'Logged in users' entry from the Sharing page.
        """
        info = super(SharingView, self).existing_role_settings()
        result =  filter(lambda v: v['id'] != AUTH_GROUP, info)
        return result
