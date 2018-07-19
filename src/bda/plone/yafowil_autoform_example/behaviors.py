from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import provider


_ = MessageFactory('bda.plone.yafowil_autoform_example')


@provider(IFormFieldProvider)
class IYafowilAutoformExampleBehavior(model.Schema):
    model.fieldset(
        'autoform_example',
        fields=['autoform_example_field'])

    autoform_example_field = schema.TextLine(
        title=_(
            u'autoform_example_field',
            default=u'Autoform Example Field'
        ),
        description=_(
            u'autoform_example_field_description',
            default=u'Autoform Example Field Description'
        ),
        required=False)
