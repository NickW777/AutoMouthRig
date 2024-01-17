import bpy
from ..types.Profile import Profile
class SetupProperties(bpy.types.PropertyGroup):
    
    shapeKeyObject : bpy.props.PointerProperty(type= bpy.types.Object, name= "Shape Key Object", description= 'TODO')#TODO
    riggedObject : bpy.props.PointerProperty(type= bpy.types.Object, name= "Rigged Object", description= 'TODO')#TODO
    armature : bpy.props.PointerProperty(type= bpy.types.Object, name= "Armature", description= 'TODO')#TODO
    
    profiles : bpy.props.CollectionProperty(type=Profile, description='TODO')#TODO
    activeIndex : bpy.props.IntProperty()