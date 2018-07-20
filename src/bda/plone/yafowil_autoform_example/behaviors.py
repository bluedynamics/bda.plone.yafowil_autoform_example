from node.utils import UNSET
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from yafowil.base import factory
from yafowil.plone.autoform import directives
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import provider


_ = MessageFactory('bda.plone.yafowil_autoform_example')


def autoform_field_1_value(context, widget, data):
    """Getter function for ``IYafowilAutoformExampleBehavior.autoform_field_1``
    value.
    """
    return context.autoform_field_1


def autoform_field_1_vocab(context, widget, data):
    """Getter function for ``IYafowilAutoformExampleBehavior.autoform_field_1``
    vocabulary.
    """
    return [
        ('opt_1', _('opt_1', default=u'Option 1')),
        ('opt_2', _('opt_2', default=u'Option 2')),
        ('opt_3', _('opt_3', default=u'Option 3'))
    ]


def autoform_field_2_factory(context):
    """Factory callback for ``IYafowilAutoformExampleBehavior.autoform_field_2``.
    """
    value = context.autoform_field_2
    value = value if value else []
    array = factory('#field:#array',
        name='autoform_field_2',
        value=value,
        props={
            'label': _(u'autoform_field_2', default=u'Autoform Field 2'),
            'array.label': ' ',
            'help': _(u'autoform_field_2_description',
                      default=u'Autoform Field 2 Description'),
            'required': _(u'autoform_field_2_required',
                          default=u'Autoform Field 2 must at least contain one entry'),
            'persist': True
        })
    array['field'] = factory(
        '#arrayfield:text',
        props={
            'label': _(u'autoform_field_2_entry', default=u'Entry'),
            'help': _(u'autoform_field_2_entry_help', default=u'Array Entry'),
            'required': _(u'autoform_field_2_entry_required',
                          default=u'Array Entry cannot be empty'),
        })
    return array


@provider(IFormFieldProvider)
class IYafowilAutoformExampleBehavior(model.Schema):

    autoform_field_1 = schema.TextLine(required=False)
    directives.order(
        'autoform_field_1',
        fieldset='default',
        after='title'
    )
    directives.factory(
        'autoform_field_1',
        blueprints='#field:select',
        value=autoform_field_1_value,
        props={
            'label': _(u'autoform_field_1', default=u'Autoform Field 1'),
            'help': _(u'autoform_field_1_description',
                      default=u'Autoform Field 1 Description'),
            'vocabulary': autoform_field_1_vocab
        }
    )

    autoform_field_2 = schema.Tuple(required=False)
    directives.order(
        'autoform_field_2',
        fieldset='default',
        after='autoform_field_1'
    )
    directives.factory_callable(
        'autoform_field_2',
        autoform_field_2_factory
    )
