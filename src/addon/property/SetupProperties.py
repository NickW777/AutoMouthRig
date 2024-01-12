import bpy
class SetupProperties(bpy.types.PropertyGroup):
    
    shapeKeyObject : bpy.props.PointerProperty(type= bpy.types.Object, name= "Shape Key Object", description= 'TODO')#TODO
    riggedObject : bpy.props.PointerProperty(type= bpy.types.Object, name= "Rigged Object", description= 'TODO')#TODO
    armature : bpy.props.PointerProperty(type= bpy.types.Object, name= "Armature", description= 'TODO')#TODO
    
    def getListRight(scene, context):
        items = []
        for s in scene.shapeKeyObject.data.shape_keys.key_blocks[1:]:
            items.append((f'+X{s.name}',s.name,"TODO"))#TODO
        return items
    
    def getListLeft(scene, context):
        items = []
        for s in scene.shapeKeyObject.data.shape_keys.key_blocks[1:]:
            items.append((f'-X{s.name}',s.name,"TODO"))#TODO
        return items
    
    def getListUp(scene, context):
        items = []
        for s in scene.shapeKeyObject.data.shape_keys.key_blocks[1:]:
            items.append((f'+Z{s.name}',s.name,"TODO"))#TODO
        return items
    
    def getListDown(scene, context):
        items = []
        for s in scene.shapeKeyObject.data.shape_keys.key_blocks[1:]:
            items.append((f'-Z{s.name}',s.name,"TODO"))#TODO
        return items