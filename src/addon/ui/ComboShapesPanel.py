import bpy
from bpy.types import Panel
from bpy.types import UIList
from ..operator.ComboShapesOperator import AddComboShapeOperator
from ..operator.ComboShapesOperator import RemoveComboShapeOperator
from ..operator.ComboShapesOperator import GenerateComboShapeDrivers

class COMBOSHAPES_UL_list(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            col = layout.column()
            col.label(text="", translate=False, icon='SHAPEKEY_DATA')
            col = layout.column()
            col.prop(item, "comboShape")
            
            col = layout.column()
            col.label(text="", translate=False, icon='SHAPEKEY_DATA')
            col = layout.column()
            col.prop(item, "driverLeft")
            
            col = layout.column()
            col.label(text="", translate=False, icon='SHAPEKEY_DATA')
            col = layout.column()
            col.prop(item, "driverRight")
        elif self.layout_type == 'GRID':
            layout.label(text='UNSUPPORTED')

class ComboShapesPanel(Panel):
    bl_label = "Add Combo Shapes"
    bl_idname = "AUTO_MOUTH_RIGGER_PT_combo_shapes_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Rigging"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        comboShapesProps = scene.comboShapesProps

        row = layout.row()
        row.prop(comboShapesProps, "shapeKeyObject")

        if comboShapesProps.shapeKeyObject is not None:
            row = layout.row()
            col = row.column()
            col.label(text='Combo Shape Key')
            col = row.column()
            col.label(text='Driving Shape Key')
            col = row.column()
            col.label(text='Driving Shape Key')
            row = layout.row()
            row.template_list("COMBOSHAPES_UL_list", "", comboShapesProps, "myCollection", comboShapesProps, "activeIndex", rows=3)
            
            col = row.column(align= True)
            col.operator(AddComboShapeOperator.bl_idname, icon='ADD', text='')
            col.operator(RemoveComboShapeOperator.bl_idname, icon='REMOVE', text='')
            
            row = layout.row()
            row.operator(GenerateComboShapeDrivers.bl_idname)

        