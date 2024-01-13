from typing import Set
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

def transferShapeKeyWithVertexGroup(shapeKeys, vertexGroup, oldName, newName, sourceObj, targetObj):
    shapeKeys[oldName].value = 1
    shapeKeys[oldName].vertex_group = vertexGroup.name
    
    bpy.ops.object.select_all(action='DESELECT')
    sourceObj.select_set(True)
    targetObj.select_set(True)
    
    bpy.context.view_layer.objects.active = targetObj
    bpy.ops.object.join_shapes()
    newShapeKey = targetObj.data.shape_keys.key_blocks[sourceObj.name]
    newShapeKey.name = newName
    
    shapeKeys[oldName].value = 0
    shapeKeys[oldName].vertex_group = ''
    
    return newShapeKey

class GenerateControlsOperator(bpy.types.Operator):
    bl_idname = "automouthrigger.gen_controls"
    bl_label = "Generate Mouth Controls"
    bl_description = 'TODO'#TODO

    def execute(self, context):
        bpy.context.view_layer.objects.selected = []
        
        scene = context.scene
        mouthShapes = scene.mouthShapes
        setup = scene.setup
        state = scene.state
        comboShapes = scene.comboShapes
        
        state.isGenerated = True

        shapesObj = setup.shapeKeyObject
        riggedObj = setup.riggedObject
        vertexGrp = shapesObj.vertex_groups
        
        shapeKeys = shapesObj.data.shape_keys.key_blocks
        
        #Each element in transforms is of the form '+XName'
        #So transforms[i][2:] gives just the 'Name' of the ith shape key 
        transforms = [mouthShapes.rightShapeKey, mouthShapes.leftShapeKey, mouthShapes.upShapeKey, mouthShapes.downShapeKey]

        amtr = scene.objects[setup.armature.name]

        for key in shapeKeys:
            key.value = 0
            key.vertex_group = ''
            
        for vg in vertexGrp:
            boneName = f'CTRL_{vg.name}'
            createBone(amtr, boneName, mouthShapes.activationDistance)   
            
            state.createdBones.add().value = boneName

            for str in transforms:
                name = getShapeName(vg, str)
                state.createdShapeKeys.add().value = name
                
                newShapeKey = transferShapeKeyWithVertexGroup(shapeKeys=shapeKeys, vertexGroup=vg, oldName=str[2:], newName=name, sourceObj=shapesObj, targetObj=riggedObj)
                
                expression = f'{str[0]}var/{mouthShapes.activationDistance}'
                transform = f'LOC_{str[1]}'
                
                addTransformDriver(amtr, newShapeKey, boneName, expression, transform) 

            for row in comboShapes.myCollection:
                comboShape = row.comboShape
                leftShape = row.driverLeft
                rightShape = row.driverRight
                
                comboName = getShapeName(vg, comboShape)
                state.createdShapeKeys.add().value = comboName
                
                newShapeKey = transferShapeKeyWithVertexGroup(shapeKeys=shapeKeys, vertexGroup=vg, oldName=comboShape, newName=comboName, sourceObj=shapesObj, targetObj=riggedObj)
                
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
    
class DeleteControlsOperator(bpy.types.Operator):
    bl_idname = "automouthrigger.del_controls"
    bl_label = "Delete Mouth Controls"
    bl_description = 'TODO'#TODO
    
    def execute(self, context):
        
        scene = context.scene
        state = scene.state
        state.isGenerated = False
        
        setup = scene.setup
        riggedObj = setup.riggedObject
        armature = setup.armature
        
        
        #Go into edit mode on the armature
        armature.select_set(True)
        bpy.context.view_layer.objects.active = armature
        bpy.ops.object.mode_set(mode='EDIT')
        
        #Select all the created bones
        for boneName in state.createdBones:
            armature.data.edit_bones[boneName.value].select = True
        
        #Delete selected bones
        bpy.ops.armature.delete()
        
        #Leave edit mode and deselect everything
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        
        
        
        
        return {'FINISHED'}