import bpy
from bpy.types import Panel
from ..operator.ButtonOperator import ButtonOperator

class MainPanel(Panel):
    bl_label = "Main Panel"
    bl_idname = "AUTO_MOUTH_RIGGER_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Rigging"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        myTool = scene.myTool

        row = layout.row()
        row.prop(myTool, "shapeKeyObject")
        
        row = layout.row()
        row.prop(myTool, "riggedObject")
        
        row = layout.row()
        row.prop(myTool, "armature")
        
        if myTool.shapeKeyObject is not None and myTool.riggedObject is not None and myTool.armature is not None:
            row = layout.row()
            row.prop(myTool, "upShapeKey")
        
            row = layout.row()
            row.prop(myTool, "leftShapeKey")
            row.prop(myTool, "rightShapeKey")
            
            row = layout.row()
            row.prop(myTool, "downShapeKey")
            
            row = layout.row()
            row.prop(myTool, "activationDistance")
            
            row = layout.row()
            row.operator(ButtonOperator.bl_idname, text="Generate Mouth Controls", icon='SPHERE')
        