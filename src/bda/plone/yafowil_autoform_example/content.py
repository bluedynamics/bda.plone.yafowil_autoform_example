from bda.plone.yafowil_autoform_example.interfaces import IYafowilAutoformExample
from plone.dexterity.content import Item
from zope.interface import implementer


@implementer(IYafowilAutoformExample)
class YafowilAutoformExample(Item):
    """Example Content.
    """
