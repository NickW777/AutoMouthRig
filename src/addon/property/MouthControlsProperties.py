import bpy
class MouthControlsProperties(bpy.types.PropertyGroup):
    def getListRight(scene, context):
        items = []
        for s in context.scene.setupProps.shapeKeyObject.data.shape_keys.key_blocks[1:]:
            items.append((f'+X{s.name}',s.name,"TODO"))#TODO
        return items
    
    def getListLeft(scene, context):
        items = []
        for s in context.scene.setupProps.shapeKeyObject.data.shape_keys.key_blocks[1:]:
            items.append((f'-X{s.name}',s.name,"TODO"))#TODO
        return items
    
    def getListUp(scene, context):
        items = []
        for s in context.scene.setupProps.shapeKeyObject.data.shape_keys.key_blocks[1:]:
            items.append((f'+Z{s.name}',s.name,"TODO"))#TODO
        return items
    
    def getListDown(scene, context):
        items = []
        for s in context.scene.setupProps.shapeKeyObject.data.shape_keys.key_blocks[1:]:
            items.append((f'-Z{s.name}',s.name,"TODO"))#TODO
        return items
    
    
    rightShapeKey : bpy.props.EnumProperty(name= 'Right', description='TODO', items= getListRight) #+X#TODO
    leftShapeKey : bpy.props.EnumProperty(name= "Left", description='TODO', items= getListLeft) #-X#TODO
    upShapeKey : bpy.props.EnumProperty(name= 'Up', description='TODO', items= getListUp) #+Z#TODO
    downShapeKey : bpy.props.EnumProperty(name= 'Down', description='TODO', items= getListDown) #-Z#TODO
    
    activationDistance: bpy.props.FloatProperty(name= 'Activation Distance', description= 'TODO', min= 0, soft_max= 0.2, default= 0.05)#TODO