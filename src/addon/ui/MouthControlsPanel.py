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
        setup = scene.setup
        mouthControls = scene.mouthControls
        
        if setup.shapeKeyObject is not None and setup.riggedObject is not None and setup.armature is not None:
            row = layout.row()
            row.prop(mouthControls, "upShapeKey")
        
            row = layout.row()
            row.prop(mouthControls, "leftShapeKey")
            row.prop(mouthControls, "rightShapeKey")
            
            row = layout.row()
            row.prop(mouthControls, "downShapeKey")
            
            row = layout.row()
            row.prop(mouthControls, "activationDistance")
            
            row = layout.row()
            row.operator(ButtonOperator.bl_idname, text="Generate Mouth Controls")
        