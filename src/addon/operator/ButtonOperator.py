import bpy

def createBone(armature, boneName, activationDist):
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature
    
    bpy.ops.object.mode_set(mode='EDIT')
    
    newBone = armature.data.edit_bones.new(boneName)

    newBone.head = (0, -0.3 - activationDist, 1.5)
    newBone.tail = (0, -0.3, 1.5)
    
    bpy.ops.object.mode_set(mode='POSE')
    
    limitLoc = armature.pose.bones.get(boneName).constraints.new('LIMIT_LOCATION')
    
    limitLoc.use_transform_limit = True
    limitLoc.owner_space = 'LOCAL'
    
    limitLoc.use_min_x = True
    limitLoc.use_max_x = True
    limitLoc.min_x = -activationDist
    limitLoc.max_x = activationDist
    
    limitLoc.use_min_y = True
    limitLoc.use_max_y = True
    limitLoc.min_y = 0
    limitLoc.max_y = 0
    
    limitLoc.use_min_z = True
    limitLoc.use_max_z = True
    limitLoc.min_z = -activationDist
    limitLoc.max_z = activationDist
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
    bpy.ops.object.select_all(action='DESELECT')
    
def addDriver(amtr, shapeKey, boneName, expression, transform):
    driver = shapeKey.driver_add('value')
    driver.driver.type = 'SCRIPTED'
    driver.driver.expression = expression
    
    var = driver.driver.variables.new()
    var.type = 'TRANSFORMS'
    var.targets[0].id = amtr
    var.targets[0].bone_target = boneName
    var.targets[0].transform_type = transform
    var.targets[0].transform_space = 'LOCAL_SPACE'

class ButtonOperator(bpy.types.Operator):
    bl_idname = "automouthrigger.gen_mouth_controls"
    bl_label = "Generate Mouth Controls"

    def execute(self, context):
        bpy.context.view_layer.objects.selected = []
        
        scene = context.scene
        myTool = scene.myTool

        shapesObj = scene.objects[myTool.shapeKeyObject.name]
        vertexGrp = shapesObj.vertex_groups
        
        shapeKeys = shapesObj.data.shape_keys.key_blocks
        transforms = [myTool.rightShapeKey, myTool.leftShapeKey, myTool.upShapeKey, myTool.downShapeKey]

        riggedObj = scene.objects[myTool.riggedObject.name]

        amtr = scene.objects[myTool.armature.name]

        for key in shapeKeys:
            key.value = 0
            key.vertex_group = ''
            
        for vg in vertexGrp:
            boneName = f'CTRL_{vg.name}'
            createBone(amtr, boneName, myTool.activationDistance)
            
            for i in range(len(transforms)):
                name = f'{vg.name}_{transforms[i]}'
                shapeKeys[transforms[i][2:]].value = 1
                shapeKeys[transforms[i][2:]].vertex_group = vg.name
                
                bpy.ops.object.select_all(action='DESELECT')
                shapesObj.select_set(True)
                riggedObj.select_set(True)
                
                bpy.context.view_layer.objects.active = riggedObj
                bpy.ops.object.join_shapes()
                newShapeKey = riggedObj.data.shape_keys.key_blocks[shapesObj.name]
                newShapeKey.name = name
                
                shapeKeys[transforms[i][2:]].value = 0
                shapeKeys[transforms[i][2:]].vertex_group = ''
                
                expression = f'{transforms[i][0]}var/{myTool.activationDistance}'
                transform = f'LOC_{transforms[i][1]}'
                
                addDriver(amtr, newShapeKey, boneName, expression, transform)
        return {'FINISHED'}