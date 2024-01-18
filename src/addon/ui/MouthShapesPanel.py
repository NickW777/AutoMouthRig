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
        profile = setup.profiles[setup.activeIndex] if len(setup.profiles) > 0 else None
        if profile is None:
            layout.label(text="No profile selected")
            return
        mouthShapes = profile.mouthShapes
        
        if profile.shapeKeyObject is not None and profile.riggedObject is not None and profile.armature is not None:
            row = layout.row()
            row.prop(mouthShapes, "upShapeKey")
        
            row = layout.row()
            row.prop(mouthShapes, "leftShapeKey")
            row.prop(mouthShapes, "rightShapeKey")
            
            row = layout.row()
            row.prop(mouthShapes, "downShapeKey")
            
            row = layout.row()
            row.prop(mouthShapes, "activationDistance")