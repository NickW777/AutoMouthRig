from typing import Set
import bpy
from bpy.types import Context, Operator

class AddComboShapeOperator(Operator):
    bl_idname = "auto_mouth_rigger.add_combo_shape"
    bl_label = "Add Combo Shape"
    bl_description = 'TODO'
    
    def execute(self, context):
        scene = context.scene
        comboShapesProps = scene.comboShapesProps
        newItem = comboShapesProps.myCollection.add()
        newItem.name = 'New Item'
        comboShapesProps.activeIndex = len(comboShapesProps.myCollection) - 1
        return {'FINISHED'}
    
class RemoveComboShapeOperator(Operator):
    bl_idname = "auto_mouth_rigger.remove_combo_shape"
    bl_label = 'Remove Combo Shape'
    bl_description = 'TODO'
    
    def execute(self, context):
        scene = context.scene
        comboShapesProps = scene.comboShapesProps
        comboShapesProps.myCollection.remove(comboShapesProps.activeIndex)
        comboShapesProps.activeIndex -= 1
        return {'FINISHED'}

class GenerateComboShapeDriversOperator(Operator):
    bl_idname = "auto_mouth_rigger.generate_combo_shape_drivers"
    bl_label = 'Generate Combo Shape Drivers'
    bl_description = 'TODO'#TODO
    
    def execute(self, context):
        scene = context.scene
        comboShapesProps = scene.comboShapesProps
        shapesObj = scene.objects[comboShapesProps.shapeKeyObject.name]
        shapeKeys = shapesObj.data.shape_keys.key_blocks
        for row in comboShapesProps.myCollection:
            driver = shapeKeys[row.comboShape].driver_add('value').driver
            driver.type = 'SCRIPTED'
            driver.expression = 'left*right'
            
            leftVar = driver.variables.new()
            leftVar.type = 'SINGLE_PROP'
            leftVar.name = 'left'
            leftVar.targets[0].id = shapesObj
            leftVar.targets[0].data_path = f'data.shape_keys.key_blocks["{row.driverLeft}"].value'
            
            rightVar = driver.variables.new()
            rightVar.type = 'SINGLE_PROP'
            rightVar.name = 'right'
            rightVar.targets[0].id = shapesObj
            rightVar.targets[0].data_path = f'data.shape_keys.key_blocks["{row.driverRight}"].value'
        
        return {'FINISHED'}