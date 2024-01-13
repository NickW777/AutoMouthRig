from typing import Set
import bpy
from bpy.types import Context, Operator

class AddComboShapeOperator(Operator):
    bl_idname = "auto_mouth_rigger.add_combo_shape"
    bl_label = "Add Combo Shape"
    bl_description = 'TODO'
    
    def execute(self, context):
        scene = context.scene
        comboShapes = scene.comboShapes
        newItem = comboShapes.myCollection.add()
        newItem.name = 'New Item'
        comboShapes.activeIndex = len(comboShapes.myCollection) - 1
        return {'FINISHED'}
    
class RemoveComboShapeOperator(Operator):
    bl_idname = "auto_mouth_rigger.remove_combo_shape"
    bl_label = 'Remove Combo Shape'
    bl_description = 'TODO'
    
    def execute(self, context):
        scene = context.scene
        comboShapes = scene.comboShapes
        comboShapes.myCollection.remove(comboShapes.activeIndex)
        comboShapes.activeIndex -= 1
        return {'FINISHED'}