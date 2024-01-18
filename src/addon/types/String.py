import bpy
from bpy.types import PropertyGroup

class String(PropertyGroup):
    value: bpy.props.StringProperty()