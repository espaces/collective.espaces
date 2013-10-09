from five import grok
from collective.spaces.browser.createform import CreateSpaceForm

grok.templatedir('.')

class CustomCreateSpaceForm(CreateSpaceForm):
    """ Extend and customise the Space creation form.
    """
    grok.template('create-space')

