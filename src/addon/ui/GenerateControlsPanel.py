import bpy
from bpy.types import Panel
from ..operator.ButtonOperator import ButtonOperator

class GenerateControlsPanel(Panel):
    bl_label = "Generate Controls"
    bl_idname = "AUTO_MOUTH_RIGGER_PT_generate_controls_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "AutoMouthRig"

    def draw(self, context):
        layout = self.layout
            
        row = layout.row()
        row.operator(ButtonOperator.bl_idname, text="Generate Mouth Controls")
        