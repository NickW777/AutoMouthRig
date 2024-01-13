import bpy
from bpy.types import PropertyGroup

class AddonStateProperties(PropertyGroup):
    isGenerated: bpy.props.BoolProperty(default=False)
    
    createdShapeKeys: []
    createdBones: []
    
    
