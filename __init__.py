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
    "version" : (0, 0, 4),
    "location" : "",
    "warning" : "",
    "category" : "Rigging"
}

import bpy

from .src.addon.properties.ComboShapesProperties import ComboShapeKey
from .src.addon.properties.AddonStateProperties import Strings
from .src.addon.ui.ComboShapesPanel import COMBOSHAPES_UL_list
from .src.addon.types.Profile import Profile

from .src.addon.properties.SetupProperties import SetupProperties
from .src.addon.properties.ComboShapesProperties import ComboShapesProperties
from .src.addon.properties.MouthShapesProperties import MouthShapesProperties
from .src.addon.properties.AddonStateProperties import AddonStateProperties

from .src.addon.operator.GenerateControlsOperator import GenerateControlsOperator
from .src.addon.operator.GenerateControlsOperator import DeleteControlsOperator
from .src.addon.operator.ComboShapesOperator import AddComboShapeOperator
from .src.addon.operator.ComboShapesOperator import RemoveComboShapeOperator
from .src.addon.operator.ProfileOperator import AddProfileOperator
from .src.addon.operator.ProfileOperator import RemoveProfileOperator


from .src.addon.ui.MouthShapesPanel import MouthShapesPanel
from .src.addon.ui.SetupPanel import SetupPanel
from .src.addon.ui.ComboShapesPanel import ComboShapesPanel
from .src.addon.ui.GenerateControlsPanel import GenerateControlsPanel


__classes = [
    ComboShapeKey,
    Strings,
    Profile,

    SetupProperties,
    ComboShapesProperties,
    MouthShapesProperties,
    AddonStateProperties,
    
    COMBOSHAPES_UL_list,
    
    GenerateControlsOperator,
    DeleteControlsOperator,
    AddComboShapeOperator,
    RemoveComboShapeOperator,
    AddProfileOperator,
    RemoveProfileOperator,
    
    SetupPanel,
    MouthShapesPanel,
    ComboShapesPanel,
    GenerateControlsPanel,
    
    
]

def register():
    for cls in __classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.state = bpy.props.PointerProperty(type= AddonStateProperties)
    bpy.types.Scene.setup = bpy.props.PointerProperty(type = SetupProperties)
    bpy.types.Scene.comboShapes = bpy.props.PointerProperty(type = ComboShapesProperties)
    bpy.types.Scene.mouthShapes = bpy.props.PointerProperty(type= MouthShapesProperties)
    
    
def unregister():
    for cls in __classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.state
    del bpy.types.Scene.setup
    del bpy.types.Scene.comboShapes
    del bpy.types.Scene.mouthShapes

if __name__ == "__main__":
    register() 