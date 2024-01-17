import bpy
from bpy.types import PropertyGroup

class Profile(PropertyGroup):
    value: bpy.props.StringProperty()