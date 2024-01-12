# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Nick Wierzbowski",
    "author" : "Auto Mouth Rig",
    "description" : "",
    "blender" : (4, 0, 2),
    "version" : (0, 0, 3),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from .src.addon.operator.ButtonOperator import ButtonOperator
from .src.addon.ui.MainPanel import MainPanel
from .src.addon.ui.ComboShapesPanel import ComboShapesPanel
from .src.addon.property.MainProperties import MainProperties
from .src.addon.property.ComboShapesProperty import ComboShapesProperties
from .src.addon.property.ComboShapesProperty import ComboShapeKey
from .src.addon.operator.ComboShapesOperator import AddComboShapeOperator
from .src.addon.operator.ComboShapesOperator import RemoveComboShapeOperator
from .src.addon.operator.ComboShapesOperator import GenerateComboShapeDrivers
from .src.addon.ui.ComboShapesPanel import COMBOSHAPES_UL_list
                
__classes = [
    ComboShapeKey,
    
    MainProperties,
    ComboShapesProperties,
    
    COMBOSHAPES_UL_list,
    
    MainPanel,
    ComboShapesPanel,
    
    ButtonOperator,
    AddComboShapeOperator,
    RemoveComboShapeOperator,
    GenerateComboShapeDrivers,
]
        
def register():
    for cls in __classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.myTool = bpy.props.PointerProperty(type = MainProperties)
    bpy.types.Scene.comboShapesProps = bpy.props.PointerProperty(type = ComboShapesProperties)
    
    
def unregister():
    for cls in __classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.myTool
    del bpy.types.Scene.comboShapesProps
    

if __name__ == "__main__":
    register() 