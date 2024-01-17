from typing import Set
import bpy
from bpy.types import Context, Operator

class AddProfileOperator(Operator):
    bl_idname = "auto_mouth_rigger.add_profile"
    bl_label = "Add Profile"
    bl_description = 'TODO'
    
    def execute(self, context):
        scene = context.scene
        setup = scene.setup
        newProfile = setup.profiles.add()
        newProfile.name = 'New Profile'
        setup.activeIndex = len(setup.profiles) - 1
        return {'FINISHED'}
    
class RemoveProfileOperator(Operator):
    bl_idname = "auto_mouth_rigger.remove_profile"
    bl_label = 'Remove Profile'
    bl_description = 'TODO'
    
    def execute(self, context):
        scene = context.scene
        setup = scene.setup
        setup.profiles.remove(setup.activeIndex)
        setup.activeIndex -= 1
        return {'FINISHED'}