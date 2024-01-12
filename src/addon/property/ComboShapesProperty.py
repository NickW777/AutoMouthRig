import bpy
from bpy.types import PropertyGroup

def getList(scene, context):
        items = []
        for s in context.scene.myTool.shapeKeyObject.data.shape_keys.key_blocks[1:]:
            items.append((f'{s.name}',s.name,"TODO"))
        return items

class ComboShapeKey(PropertyGroup):
    comboShape : bpy.props.EnumProperty(name= '',  description='TODO', items= getList)
    driverLeft : bpy.props.EnumProperty(name= '',  description='TODO', items= getList)
    driverRight : bpy.props.EnumProperty(name= '',  description='TODO', items= getList)
    activeIndex : bpy.props.IntProperty()

class ComboShapesProperties(PropertyGroup):
    
    shapeKeyObject : bpy.props.PointerProperty(type= bpy.types.Object, name= "Shape Key Object", description= 'TODO')
    
    def getList(scene, context):
        items = []
        for s in context.scene.myTool.shapeKeyObject.data.shape_keys.key_blocks[1:]:
            items.append((s.name,s.name,"TODO"))
        return items
    
    myCollection : bpy.props.CollectionProperty(name= 'My Collection', description= 'TODO', type= ComboShapeKey)
    activeIndex : bpy.props.IntProperty()
