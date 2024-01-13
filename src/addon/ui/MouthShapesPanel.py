import bpy
from bpy.types import Panel

class MouthShapesPanel(Panel):
    bl_label = "Mouth Shapes"
    bl_idname = "AUTO_MOUTH_RIGGER_PT_mouth_shapes_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "AutoMouthRig"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        setup = scene.setup
        mouthShapes = scene.mouthShapes
        
        if setup.shapeKeyObject is not None and setup.riggedObject is not None and setup.armature is not None:
            row = layout.row()
            row.prop(mouthShapes, "upShapeKey")
        
            row = layout.row()
            row.prop(mouthShapes, "leftShapeKey")
            row.prop(mouthShapes, "rightShapeKey")
            
            row = layout.row()
            row.prop(mouthShapes, "downShapeKey")
            
            row = layout.row()
            row.prop(mouthShapes, "activationDistance")