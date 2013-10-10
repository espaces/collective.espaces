from zope.component.hooks import getSite
from Products.CMFCore.utils import getToolByName

PROFILE_ID = 'profile-collective.espaces:default'

def setupVarious(context, site=None):
    """
    Set up various aspects of Plone that we can't set up using
    GenericSetup profiles (yet).  These aspects should be removed
        whenever possible and replaced with a GS import profile.
    """

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('collective.espaces_various.txt') is None:
        return

    # Add additional setup code here
    site = site or getSite()

    # Show all workflow states in calendar
    site.portal_calendar.calendar_states = ['external', 'internal', 'internally_published', 'pending', 'private', 'visible', 'published']

    # Unpublish all default content
    paths = []
    for identifier in ('Members', 'events', 'news'):
        obj = site.get(identifier)
        # Content is not included by default in tests
        if obj:
            obj.getField('excludeFromNav').set(obj, True)
            obj.reindexObject()
            if obj:
                paths.append('/'.join(obj.getPhysicalPath()))

    plone_utils = getToolByName(site, 'plone_utils')
    plone_utils.transitionObjectsByPaths('retract',
                                         paths,
                                         include_children=True)
