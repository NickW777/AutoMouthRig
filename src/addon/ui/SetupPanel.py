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
        setupProps = scene.setupProps

        row = layout.row()
        row.prop(setupProps, "shapeKeyObject")
        
        row = layout.row()
        row.prop(setupProps, "riggedObject")
        
        row = layout.row()
        row.prop(setupProps, "armature")