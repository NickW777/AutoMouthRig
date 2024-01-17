import bpy
from bpy.types import PropertyGroup
from ..types.String import String
from ..properties.ComboShapesProperties import ComboShapesProperties
from ..properties.MouthShapesProperties import MouthShapesProperties

class Profile(PropertyGroup):
    value: bpy.props.StringProperty()
    
    isGenerated: bpy.props.BoolProperty(default=False)
    
    createdShapeKeys: bpy.props.CollectionProperty(type= String)
    createdBones: bpy.props.CollectionProperty(type= String)
    
    shapeKeyObject : bpy.props.PointerProperty(type= bpy.types.Object, name= "Shape Key Object", description= 'TODO')#TODO
    riggedObject : bpy.props.PointerProperty(type= bpy.types.Object, name= "Rigged Object", description= 'TODO')#TODO
    armature : bpy.props.PointerProperty(type= bpy.types.Object, name= "Armature", description= 'TODO')#TODO
    
    comboShapes: bpy.props.PointerProperty(type = ComboShapesProperties)
    mouthShapes: bpy.props.PointerProperty(type = MouthShapesProperties)