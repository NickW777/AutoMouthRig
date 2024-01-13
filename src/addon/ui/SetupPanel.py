import bpy
from bpy.types import Panel
from ..operator.ButtonOperator import ButtonOperator

class SetupPanel(Panel):
    bl_label = "Setup"
    bl_idname = "AUTO_MOUTH_RIGGER_PT_setup_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "AutoMouthRig"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        setup = scene.setup

        row = layout.row()
        row.prop(setup, "shapeKeyObject")
        
        row = layout.row()
        row.prop(setup, "riggedObject")
        
        row = layout.row()
        row.prop(setup, "armature")