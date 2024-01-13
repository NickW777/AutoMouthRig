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
    
def addTransformDriver(amtr, shapeKey, boneName, expression, transform):
    driver = shapeKey.driver_add('value')
    driver.driver.type = 'SCRIPTED'
    driver.driver.expression = expression
    
    var = driver.driver.variables.new()
    var.type = 'TRANSFORMS'
    var.targets[0].id = amtr
    var.targets[0].bone_target = boneName
    var.targets[0].transform_type = transform
    var.targets[0].transform_space = 'LOCAL_SPACE'
    
def getShapeName(vertexGroup, originalShape):
    return f'{vertexGroup.name}_{originalShape}'

class ButtonOperator(bpy.types.Operator):
    bl_idname = "automouthrigger.gen_mouth_controls"
    bl_label = "Generate Mouth Controls"
    bl_description = 'TODO'#TODO

    def execute(self, context):
        bpy.context.view_layer.objects.selected = []
        
        scene = context.scene
        mouthControlsProps = scene.mouthControlsProps
        setupProps = scene.setupProps
        comboShapesProps = scene.comboShapesProps

        shapesObj = setupProps.shapeKeyObject
        riggedObj = setupProps.riggedObject
        vertexGrp = shapesObj.vertex_groups
        
        shapeKeys = shapesObj.data.shape_keys.key_blocks
        
        
        
        #Each element in transforms is of the form '+XName'
        #So transforms[i][2:] gives just the 'Name' of the ith shape key 
        transforms = [mouthControlsProps.rightShapeKey, mouthControlsProps.leftShapeKey, mouthControlsProps.upShapeKey, mouthControlsProps.downShapeKey]

        amtr = scene.objects[setupProps.armature.name]

        for key in shapeKeys:
            key.value = 0
            key.vertex_group = ''
            
        for vg in vertexGrp:
            boneName = f'CTRL_{vg.name}'
            createBone(amtr, boneName, mouthControlsProps.activationDistance)

            for str in transforms:
                shapeName = getShapeName(vg, str)
                shapeKeys[str[2:]].value = 1
                shapeKeys[str[2:]].vertex_group = vg.name
                
                bpy.ops.object.select_all(action='DESELECT')
                shapesObj.select_set(True)
                riggedObj.select_set(True)
                
                bpy.context.view_layer.objects.active = riggedObj
                bpy.ops.object.join_shapes()
                newShapeKey = riggedObj.data.shape_keys.key_blocks[shapesObj.name]
                newShapeKey.name = shapeName
                
                shapeKeys[str[2:]].value = 0
                shapeKeys[str[2:]].vertex_group = ''
                
                expression = f'{str[0]}var/{mouthControlsProps.activationDistance}'
                transform = f'LOC_{str[1]}'
                
                addTransformDriver(amtr, newShapeKey, boneName, expression, transform)

            for row in comboShapesProps.myCollection:
                comboShape = row.comboShape
                leftShape = row.driverLeft
                rightShape = row.driverRight
                
                comboName = getShapeName(vg, comboShape)
                
                shapeKeys[comboShape].value = 1
                shapeKeys[comboShape].vertex_group = vg.name
                
                bpy.ops.object.select_all(action='DESELECT')
                shapesObj.select_set(True)
                riggedObj.select_set(True)
                
                bpy.context.view_layer.objects.active = riggedObj
                bpy.ops.object.join_shapes()
                newShapeKey = riggedObj.data.shape_keys.key_blocks[shapesObj.name]
                newShapeKey.name = comboName
                
                shapeKeys[comboShape].value = 0
                shapeKeys[comboShape].vertex_group = ''
                
                riggedShapeKeys = riggedObj.data.shape_keys.key_blocks
                
                driver = riggedShapeKeys[comboName].driver_add('value').driver
                driver.type = 'SCRIPTED'
                driver.expression = 'left*right'
                
                for str in transforms:
                    if str[2:] == leftShape:
                        leftVar = driver.variables.new()
                        leftVar.type = 'SINGLE_PROP'
                        leftVar.name = 'left'
                        leftVar.targets[0].id = riggedObj
                        leftVar.targets[0].data_path = f'data.shape_keys.key_blocks["{getShapeName(vg, str)}"].value'
                        
                    if str[2:] == rightShape:
                        rightVar = driver.variables.new()
                        rightVar.type = 'SINGLE_PROP'
                        rightVar.name = 'right'
                        rightVar.targets[0].id = riggedObj
                        rightVar.targets[0].data_path = f'data.shape_keys.key_blocks["{getShapeName(vg, str)}"].value'
                
                
                
                
        return {'FINISHED'}