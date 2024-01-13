import bpy
from bpy.types import Panel
from ..operator.GenerateControlsOperator import GenerateControlsOperator
from ..operator.GenerateControlsOperator import DeleteControlsOperator

class GenerateControlsPanel(Panel):
    bl_label = "Generate Controls"
    bl_idname = "AUTO_MOUTH_RIGGER_PT_generate_controls_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "AutoMouthRig"

    def draw(self, context):
        scene = context.scene
        state = scene.state
        layout = self.layout
            
        row = layout.row()
        if state.isGenerated:
            row.operator(DeleteControlsOperator.bl_idname)
        else:
            row.operator(GenerateControlsOperator.bl_idname)
        