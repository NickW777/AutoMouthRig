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
    "name" : "Auto Mouth Rig",
    "author" : "Nick Wierzbowski",
    "description" : "",
    "blender" : (4, 0, 2),
    "version" : (0, 0, 3),
    "location" : "",
    "warning" : "",
    "category" : "Rigging"
}

import bpy

from .src.addon.property.ComboShapesProperty import ComboShapeKey
from .src.addon.ui.ComboShapesPanel import COMBOSHAPES_UL_list

from .src.addon.property.SetupProperties import SetupProperties
from .src.addon.property.ComboShapesProperty import ComboShapesProperties
from .src.addon.property.MouthControlsProperties import MouthControlsProperties

from .src.addon.operator.ButtonOperator import ButtonOperator
from .src.addon.operator.ComboShapesOperator import AddComboShapeOperator
from .src.addon.operator.ComboShapesOperator import RemoveComboShapeOperator
# from .src.addon.operator.ComboShapesOperator import GenerateComboShapeDriversOperator

from .src.addon.ui.MouthControlsPanel import MouthControlsPanel
from .src.addon.ui.SetupPanel import SetupPanel
from .src.addon.ui.ComboShapesPanel import ComboShapesPanel


__classes = [
    ComboShapeKey,

    SetupProperties,
    ComboShapesProperties,
    MouthControlsProperties,
    
    COMBOSHAPES_UL_list,
    
    SetupPanel,
    ComboShapesPanel,
    MouthControlsPanel,
    
    ButtonOperator,
    AddComboShapeOperator,
    RemoveComboShapeOperator,
    # GenerateComboShapeDriversOperator,
]

def register():
    for cls in __classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.setupProps = bpy.props.PointerProperty(type = SetupProperties)
    bpy.types.Scene.comboShapesProps = bpy.props.PointerProperty(type = ComboShapesProperties)
    bpy.types.Scene.mouthControlsProps = bpy.props.PointerProperty(type= MouthControlsProperties)
    
    
def unregister():
    for cls in __classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.setupProps
    del bpy.types.Scene.comboShapesProps
    del bpy.types.Scene.mouthControlsProps

if __name__ == "__main__":
    register() 