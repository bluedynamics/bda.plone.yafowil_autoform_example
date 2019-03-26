from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from yafowil.plone.autoform.form import DisplayAutoForm


class YafowilExampleView(DisplayAutoForm):
    skip_fields = ['title', 'description']
    template = ViewPageTemplateFile('autoform_example_view.pt')

    def __call__(self):
        return self.template()
