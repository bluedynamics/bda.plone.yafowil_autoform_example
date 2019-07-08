from bda.plone.yafowil_autoform_example.interfaces import IYafowilAutoformExample
from plone.dexterity.content import Item
from plone.dexterity.content import Container
from zope.interface import implementer


@implementer(IYafowilAutoformExample)
class YafowilAutoformExample(Container):
# class YafowilAutoformExample(Item):
    """Example Content.
    """
