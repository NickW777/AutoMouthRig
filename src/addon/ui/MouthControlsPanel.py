import bpy
from bpy.types import Panel
from ..operator.ButtonOperator import ButtonOperator

class MouthControlsPanel(Panel):
    bl_label = "Mouth Controls"
    bl_idname = "AUTO_MOUTH_RIGGER_PT_mouth_controls_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "AutoMouthRig"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        setupProps = scene.setupProps
        
        if setupProps.shapeKeyObject is not None and setupProps.riggedObject is not None and setupProps.armature is not None:
            row = layout.row()
            row.prop(setupProps, "upShapeKey")
        
            row = layout.row()
            row.prop(setupProps, "leftShapeKey")
            row.prop(setupProps, "rightShapeKey")
            
            row = layout.row()
            row.prop(setupProps, "downShapeKey")
            
            row = layout.row()
            row.prop(setupProps, "activationDistance")
            
            row = layout.row()
            row.operator(ButtonOperator.bl_idname, text="Generate Mouth Controls")
        