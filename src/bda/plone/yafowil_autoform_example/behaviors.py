from node.utils import UNSET
from plone.app.dexterity.behaviors.metadata import IDublinCore
from plone.app.textfield import RichText as RichTextField
from plone.app.z3cform.widget import RichTextFieldWidget
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from yafowil.base import factory
from yafowil.plone.autoform import directives
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import provider


_ = MessageFactory('bda.plone.yafowil_autoform_example')


###############################################################################
# Selection field example
###############################################################################

def selection_field_value(context, widget, data):
    """Getter function for ``IYafowilSelectionFieldBehavior.selection_field``
    value.
    """
    return context.selection_field


def selection_field_vocab(context, widget, data):
    """Getter function for ``.IYafowilSelectionFieldBehaviorselection_field``
    vocabulary.
    """
    return [
        ('opt_1', _('opt_1', default=u'Option 1')),
        ('opt_2', _('opt_2', default=u'Option 2')),
        ('opt_3', _('opt_3', default=u'Option 3'))
    ]


@provider(IFormFieldProvider)
class IYafowilSelectionFieldBehavior(model.Schema):

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


###############################################################################
# Relation field example
###############################################################################

def relation_field_value(context, widget, data):
    """Getter function for ``IYafowilRelationFieldBehavior.relation_field``
    value.
    """
    return context.relation_field


@provider(IFormFieldProvider)
class IYafowilRelationFieldBehavior(model.Schema):

    relation_field = RelationChoice(required=False, values=[])
    directives.factory(
        'relation_field',
        blueprints='#field:relation',
        value=relation_field_value,
        props={
            'label': _(u'relation_field', default=u'Relation Field'),
            'help': _(u'relation_field_description',
                      default=u'Relation Field Description'),
            'context': lambda context, widget, data: context
        }
    )


###############################################################################
# Text array field example
###############################################################################

def text_array_field_factory(context):
    """Factory callback for ``IYafowilTextArrayFieldBehavior.text_array_field``.
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


@provider(IFormFieldProvider)
class IYafowilTextArrayFieldBehavior(model.Schema):

    text_array_field = schema.Tuple(required=False)
    directives.factory_callable(
        'text_array_field',
        text_array_field_factory
    )


###############################################################################
# Select array field example
###############################################################################

def select_array_field_factory(context):
    """Factory callback for ``IYafowilSelectArrayFieldBehavior.select_array_field``.
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


@provider(IFormFieldProvider)
class IYafowilSelectArrayFieldBehavior(model.Schema):

    select_array_field = schema.Tuple(required=False)
    directives.factory_callable(
        'select_array_field',
        select_array_field_factory
    )


###############################################################################
# Compound array field example
###############################################################################

def compound_array_field_factory(context):
    """Factory callback for ``IYafowilCompoundArrayFieldBehavior.compound_array_field``.
    """
    value = context.compound_array_field
    value = value if value else []
    array = factory(
        '#field:#array',
        name='compound_array_field',
        value=value,
        props={
            'label': _(u'compound_array_field', default=u'Compound Array Field'),
            'array.label': ' ',
            'help': _(u'compound_array_field_description',
                      default=u'Compound Array Field Description'),
            'required': _(u'compound_array_field_required',
                          default=u'Compound Array Field must at least contain one entry'),
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
class IYafowilCompoundArrayFieldBehavior(model.Schema):

    compound_array_field = schema.Tuple(required=False)
    directives.factory_callable(
        'compound_array_field',
        compound_array_field_factory
    )


###############################################################################
# Relation array field example
###############################################################################

def relations_array_field_factory(context):
    """Factory callback for ``IYafowilRelationArrayFieldBehavior.relations_array_field``.
    """
    value = context.relations_array_field
    value = value if value else []
    array = factory(
        '#field:#array',
        name='relations_array_field',
        value=value,
        props={
            'label': _(u'relations_array_field', default=u'Relations Array Field'),
            'array.label': ' ',
            'help': _(u'relations_array_field_description',
                      default=u'Relations Array Field Description'),
            'required': _(u'relations_array_field_required',
                          default=u'Relations Array Field must at least contain one entry'),
            'persist': True
        })
    relations = array['compound'] = factory('compound')
    relations['field_1'] = factory(
        '#arrayfield:text',
        props={
            'label': _(u'textfield', default=u'Textfield')
        })
    relations['field_2'] = factory(
        '#arrayfield:#arrayrelation',
        props={
            'label': _(u'relation', default=u'Relation'),
            'context': context
        })
    return array


@provider(IFormFieldProvider)
class IYafowilRelationArrayFieldBehavior(model.Schema):

    relations_array_field = RelationList(required=False)
    directives.factory_callable(
        'relations_array_field',
        relations_array_field_factory
    )


###############################################################################
# Richtext array field example
###############################################################################

def richtext_array_field_factory(context):
    """Factory callback for ``IYafowilRichtextArrayFieldBehavior.relations_array_field``.
    """
    value = context.richtext_array_field
    value = value if value else []
    array = factory(
        '#field:#array',
        name='richtext_array_field',
        value=value,
        props={
            'label': _(u'richtext_array_field', default=u'Richtext Array Field'),
            'array.label': ' ',
            'help': _(u'richtext_array_field_description',
                      default=u'Richtext Array Field Description'),
            'required': _(u'richtext_array_field_required',
                          default=u'Richtext Array Field must at least contain one entry'),
            'persist': True
        })
    array['field'] = factory(
        '#arrayfield:#arrayrichtext',
        props={
            'label': _(u'richtext_array_field_entry', default=u'Entry'),
            'pattern_options': {
                'tiny': {
                    'menu': [],
                    'menubar': [],
                    'plugins': [],
                    'toolbar': 'bold italic'
                }
            },
            'context': context
        })
    return array


@provider(IFormFieldProvider)
class IYafowilRichtextArrayFieldBehavior(model.Schema):

    richtext_array_field = schema.Tuple(required=False)
    directives.factory_callable(
        'richtext_array_field',
        richtext_array_field_factory
    )


###############################################################################
# combined behaviors example
###############################################################################

@provider(IFormFieldProvider)
class IYafowilAutoformExampleBehavior(
    IYafowilSelectionFieldBehavior,
    # IYafowilRelationFieldBehavior,
    IYafowilTextArrayFieldBehavior,
    IYafowilSelectArrayFieldBehavior,
    IYafowilCompoundArrayFieldBehavior,
    IYafowilRelationArrayFieldBehavior,
    IYafowilRichtextArrayFieldBehavior
):

    # directives.order(
    #     'relation_field',
    #     fieldset='default',
    #     after='selection_field'
    # )
    directives.order(
        'text_array_field',
        fieldset='default',
        after='selection_field'
    )
    directives.order(
        'select_array_field',
        fieldset='default',
        after='text_array_field'
    )
    directives.order(
        'compound_array_field',
        fieldset='default',
        after='select_array_field'
    )
    directives.order(
        'relations_array_field',
        fieldset='default',
        after='compound_array_field'
    )
    directives.order(
        'richtext_array_field',
        fieldset='default',
        after='relations_array_field'
    )


###############################################################################
# Integration and z3cform compatibility test behaviors
###############################################################################

@provider(IFormFieldProvider)
class IRichtextCompatTestBehavior(IDublinCore):

    richtext_description = RichTextField(
        title='Rich Text Description',
        description='Rich Text Widget as Description field',
        required=False,
        missing_value=''
    )
    form.widget(
        'richtext_description',
        RichTextFieldWidget,
        pattern_options={
            'tiny': {
                'menu': [],
                'menubar': [],
                'plugins': [],
                'toolbar': 'bold italic'
            }
        }
    )
    form.order_after(richtext_description='IDublinCore.title')
    form.mode(description='hidden')
