from Products.CMFPlone.utils import getToolByName


PROFILE_ID = 'profile-collective.espaces:default'


def run_import_step(context, step):
    """Re-import some specified import step for Generic Setup.
    """
    setup = getToolByName(context, 'portal_setup')
    return setup.runImportStepFromProfile(PROFILE_ID, step)


def upgrade_0001_to_0002(context):
    # Configre the skins profile
    run_import_step(context, 'skins')

    # Install new dependencies
    qi = getToolByName(context, 'portal_quickinstaller')
    qi.installProduct('plone.formwidget.recaptcha')
    qi.installProduct('collective.registrationcaptcha')

    # Configre the new JS resources
    run_import_step(context, 'jsregistry')
