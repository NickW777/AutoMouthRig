import bpy
from bpy.types import Panel
from ..operator.ProfileOperator import AddProfileOperator, RemoveProfileOperator

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
        row.template_list("UI_UL_list", "id", setup, "profiles", setup, "activeIndex", rows=3)
        
        col = row.column(align= True)
        col.operator(AddProfileOperator.bl_idname, icon='ADD', text='')
        col.operator(RemoveProfileOperator.bl_idname, icon='REMOVE', text='') 

        row = layout.row()
        row.prop(setup, "shapeKeyObject")
        
        row = layout.row()
        row.prop(setup, "riggedObject")
        
        row = layout.row()
        row.prop(setup, "armature")