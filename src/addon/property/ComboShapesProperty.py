import bpy
from bpy.types import PropertyGroup

def getList(scene, context):
        items = []
        for s in context.scene.setupProps.shapeKeyObject.data.shape_keys.key_blocks[1:]:
            items.append((f'{s.name}',s.name,"TODO"))#TODO
        return items

class ComboShapeKey(PropertyGroup):
    comboShape : bpy.props.EnumProperty(name= '',  description='TODO', items= getList)#TODO
    driverLeft : bpy.props.EnumProperty(name= '',  description='TODO', items= getList)#TODO
    driverRight : bpy.props.EnumProperty(name= '',  description='TODO', items= getList)#TODO
    activeIndex : bpy.props.IntProperty()

class ComboShapesProperties(PropertyGroup):
    
    shapeKeyObject : bpy.props.PointerProperty(type= bpy.types.Object, name= "Shape Key Object", description= 'TODO')#TODO
    myCollection : bpy.props.CollectionProperty(name= 'My Collection', description= 'TODO', type= ComboShapeKey)#TODO
    activeIndex : bpy.props.IntProperty()
