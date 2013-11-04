from five import grok
from zope.formlib import form
from collective.aaf.auth import _generatePassword
from collective.spaces.browser.createform import CreateSpaceForm
from plone.app.users.browser.personalpreferences \
        import PasswordAccountPanel as OriginalPasswordAccountPanel


grok.templatedir('.')


class CustomCreateSpaceForm(CreateSpaceForm):
    """ Extend and customise the Space creation form.
    """
    grok.template('create-space')


class PasswordAccountPanel(OriginalPasswordAccountPanel):

    actions = form.Actions(
        form.Action('Change password',
                    success='action_reset_passwd',
                    validator='validate_password',
                    name=u'reset_passwd'),
        form.Action('Generate new password',
                    success='action_generate_passwd',
                    validator=lambda form, action, data: [],
                    name=u'generate_passwd')
    )

    def action_generate_passwd(self, action, data):
        data['new_password'] = _generatePassword(self.context)
        return self.action_reset_passwd.success_handler(self, action, data)

