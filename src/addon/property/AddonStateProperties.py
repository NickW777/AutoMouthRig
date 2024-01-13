import bpy
from bpy.types import PropertyGroup

class Strings(PropertyGroup):
    value: bpy.props.StringProperty()

class AddonStateProperties(PropertyGroup):
    isGenerated: bpy.props.BoolProperty(default=False)
    
    createdShapeKeys: bpy.props.CollectionProperty(type= Strings)
    createdBones: bpy.props.CollectionProperty(type= Strings)
    

# createdBones: []
