from Products.CMFPlone.utils import getToolByName


PROFILE_ID = 'profile-collective.espaces:default'


def run_import_step(context, step):
    """Re-import some specified import step for Generic Setup.
    """
    setup = getToolByName(context, 'portal_setup')
    return setup.runImportStepFromProfile(PROFILE_ID, step)


def upgrade_0001_to_0002(context):
    """ Install recaptcha protection on the site.
    """
    # Configre the skins profile
    run_import_step(context, 'skins')

    # Install new dependencies
    qi = getToolByName(context, 'portal_quickinstaller')
    qi.installProduct('plone.formwidget.recaptcha')
    qi.installProduct('collective.registrationcaptcha')

    # Configre the new JS resources
    run_import_step(context, 'jsregistry')


def upgrade_0002_to_0003(context):
    """ Re-import configuration registry for Discussion options.
    """
    run_import_step(context, 'plone.app.registry')


def upgrade_0003_to_0004(context):
    """ Upgrade dependencies and reconfigure portlets.
    """
    qi = getToolByName(context, 'portal_quickinstaller')
    qi.upgradeProduct('collective.aaf')
    run_import_step(context, 'portlets')

    # Change language
    ltool = getToolByName(context, 'portal_languages')
    ltool.setDefaultLanguage('en-au')


def upgrade_0004_to_0005(context):
    """ Upgrade language configuration and syndication settings.
    """
    run_import_step(context, 'languagetool')
    run_import_step(context, 'plone.app.registry')
    run_import_step(context, 'actions')
