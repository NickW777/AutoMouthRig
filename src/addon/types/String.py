import bpy
from bpy.types import PropertyGroup

class String(PropertyGroup):
    string: bpy.props.StringProperty()