import bpy
class SetupProperties(bpy.types.PropertyGroup):
    
    shapeKeyObject : bpy.props.PointerProperty(type= bpy.types.Object, name= "Shape Key Object", description= 'TODO')
    riggedObject : bpy.props.PointerProperty(type= bpy.types.Object, name= "Rigged Object", description= 'TODO')
    armature : bpy.props.PointerProperty(type= bpy.types.Object, name= "Armature", description= 'TODO')
    
    def getListRight(scene, context):
        items = []
        for s in scene.shapeKeyObject.data.shape_keys.key_blocks[1:]:
            items.append((f'+X{s.name}',s.name,"TODO"))
        return items
    
    def getListLeft(scene, context):
        items = []
        for s in scene.shapeKeyObject.data.shape_keys.key_blocks[1:]:
            items.append((f'-X{s.name}',s.name,"TODO"))
        return items
    
    def getListUp(scene, context):
        items = []
        for s in scene.shapeKeyObject.data.shape_keys.key_blocks[1:]:
            items.append((f'+Z{s.name}',s.name,"TODO"))
        return items
    
    def getListDown(scene, context):
        items = []
        for s in scene.shapeKeyObject.data.shape_keys.key_blocks[1:]:
            items.append((f'-Z{s.name}',s.name,"TODO"))
        return items
    
    
    rightShapeKey : bpy.props.EnumProperty(name= 'Right', description='TODO', items= getListRight) #+X
    leftShapeKey : bpy.props.EnumProperty(name= "Left", description='TODO', items= getListLeft) #-X
    upShapeKey : bpy.props.EnumProperty(name= 'Up', description='TODO', items= getListUp) #+Z
    downShapeKey : bpy.props.EnumProperty(name= 'Down', description='TODO', items= getListDown) #-Z
    
    activationDistance: bpy.props.FloatProperty(name= 'Activation Distance', description= 'TODO', min= 0, soft_max= 0.2, default= 0.05)