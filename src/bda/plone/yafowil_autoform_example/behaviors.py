from node.utils import UNSET
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from yafowil.base import factory
from yafowil.plone.autoform import directives
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import provider


_ = MessageFactory('bda.plone.yafowil_autoform_example')


def selection_field_value(context, widget, data):
    """Getter function for ``IYafowilAutoformExampleBehavior.selection_field``
    value.
    """
    return context.selection_field


def selection_field_vocab(context, widget, data):
    """Getter function for ``IYafowilAutoformExampleBehavior.selection_field``
    vocabulary.
    """
    return [
        ('opt_1', _('opt_1', default=u'Option 1')),
        ('opt_2', _('opt_2', default=u'Option 2')),
        ('opt_3', _('opt_3', default=u'Option 3'))
    ]


def text_array_field_factory(context):
    """Factory callback for ``IYafowilAutoformExampleBehavior.text_array_field``.
    """
    value = context.text_array_field
    value = value if value else []
    array = factory(
        '#field:#array',
        name='text_array_field',
        value=value,
        props={
            'label': _(u'text_array_field', default=u'Text Array Field'),
            'array.label': ' ',
            'help': _(u'text_array_field_description',
                      default=u'Text Array Field Description'),
            'required': _(u'text_array_field_required',
                          default=u'Text Array Field must at least contain one entry'),
            'persist': True
        })
    array['field'] = factory(
        '#arrayfield:text',
        props={
            'label': _(u'text_array_field_entry', default=u'Entry'),
            'help': _(u'text_array_field_entry_help', default=u'Array Entry'),
            'required': _(u'text_array_field_entry_required',
                          default=u'Array Entry cannot be empty'),
        })
    return array


def select_array_field_factory(context):
    """Factory callback for ``IYafowilAutoformExampleBehavior.select_array_field``.
    """
    value = context.select_array_field
    value = value if value else []
    array = factory(
        '#field:#array',
        name='select_array_field',
        value=value,
        props={
            'label': _(u'select_array_field', default=u'Select Array Field'),
            'array.label': ' ',
            'help': _(u'select_array_field_description',
                      default=u'Select Array Field Description'),
            'required': _(u'select_array_field_required',
                          default=u'Select Array Field must at least contain one entry'),
            'persist': True
        })
    array['field'] = factory(
        '#arrayfield:select',
        props={
            'label': _(u'select_array_field_entry', default=u'Entry'),
            'vocabulary': [
                ('1', 'Value 1'),
                ('2', 'Value 2'),
                ('3', 'Value 3'),
            ]
        })
    return array


def nested_array_field_factory(context):
    """Factory callback for ``IYafowilAutoformExampleBehavior.nested_array_field``.
    """
    value = context.nested_array_field
    value = value if value else []
    array = factory(
        '#field:#array',
        name='nested_array_field',
        value=value,
        props={
            'label': _(u'nested_array_field', default=u'Nested Array Field'),
            'array.label': ' ',
            'help': _(u'nested_array_field_description',
                      default=u'Nested Array Field Description'),
            'required': _(u'nested_array_field_required',
                          default=u'Nested Array Field must at least contain one entry'),
            'persist': True
        })
    compound = array['compound'] = factory('compound')
    compound['field_1'] = factory(
        '#arrayfield:text',
        props={
            'label': _(u'textfield', default=u'Textfield')
        })
    compound['field_2'] = factory(
        '#arrayfield:select',
        props={
            'label': _(u'selectfield', default=u'Selectfield'),
            'vocabulary': [
                ('1', 'Value 1'),
                ('2', 'Value 2'),
                ('3', 'Value 3'),
            ]
        })
    return array


@provider(IFormFieldProvider)
class IYafowilAutoformExampleBehavior(model.Schema):

    selection_field = schema.TextLine(required=False)
    directives.order(
        'selection_field',
        fieldset='default',
        after='title'
    )
    directives.factory(
        'selection_field',
        blueprints='#field:select',
        value=selection_field_value,
        props={
            'label': _(u'selection_field', default=u'Selection Field'),
            'help': _(u'selection_field_description',
                      default=u'Selection Field Description'),
            'vocabulary': selection_field_vocab
        }
    )

    text_array_field = schema.Tuple(required=False)
    directives.order(
        'text_array_field',
        fieldset='default',
        after='selection_field'
    )
    directives.factory_callable(
        'text_array_field',
        text_array_field_factory
    )

    select_array_field = schema.Tuple(required=False)
    directives.order(
        'select_array_field',
        fieldset='default',
        after='text_array_field'
    )
    directives.factory_callable(
        'select_array_field',
        select_array_field_factory
    )

    nested_array_field = schema.Tuple(required=False)
    directives.order(
        'nested_array_field',
        fieldset='default',
        after='select_array_field'
    )
    directives.factory_callable(
        'nested_array_field',
        nested_array_field_factory
    )
