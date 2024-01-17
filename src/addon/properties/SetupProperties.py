import bpy
from ..types.Profile import Profile
class SetupProperties(bpy.types.PropertyGroup):
    profiles : bpy.props.CollectionProperty(type=Profile, description='TODO')#TODO
    activeIndex : bpy.props.IntProperty()