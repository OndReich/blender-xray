import bpy

from .base import XRayPanel, build_label
from ..skl.ops import OpExportSkl
from ..ops import action_utils
from .. import registry


@registry.module_thing
class XRAY_PT_ActionPanel(XRayPanel):
    bl_category = 'F-Curve'
    bl_space_type = 'DOPESHEET_EDITOR' if bpy.app.version >= (2, 78, 0) else 'GRAPH_EDITOR'
    bl_region_type = 'UI'
    bl_context = 'object'
    bl_label = build_label('Action')

    @classmethod
    def poll(cls, context):
        return (
            context.active_object and
            context.active_object.animation_data and
            context.active_object.animation_data.action
        )

    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        action = obj.animation_data.action
        data = action.xray
        box = layout.column(align=True) if data.autobake != 'off' else layout
        if data.autobake_auto:
            box.prop(data, 'autobake_auto', toggle=True, icon='RENDER_STILL')
        else:
            row = box.row(align=True)
            row.prop(data, 'autobake_auto', toggle=True, text='Auto Bake:', icon='RENDER_STILL')
            text = 'On' if data.autobake_on else 'Off'
            row.prop(data, 'autobake_on', toggle=True, text=text)
        if box != layout:
            if data.autobake_custom_refine:
                row = box.row(align=True)
                row.prop(
                    data, 'autobake_custom_refine',
                    toggle=True, text='', icon='BUTS'
                )
                row.prop(data, 'autobake_refine_location', text='L')
                row.prop(data, 'autobake_refine_rotation', text='R')
            else:
                box.prop(data, 'autobake_custom_refine', toggle=True)
        layout.prop(data, 'fps')
        if obj.type != 'ARMATURE':
            return
        layout.prop(data, 'speed')
        layout.prop(data, 'accrue')
        layout.prop(data, 'falloff')
        layout.prop(data, 'flags_fx', text='Type FX', toggle=True)
        if data.flags_fx:
            row = layout.row(align=True)
            row.label(text='Start Bone:')
            row.prop_search(data, 'bonestart_name', obj.pose, 'bones', text='')
            layout.prop(data, 'power', text='Power')
        else:
            row = layout.row(align=True)
            row.label(text='Bone Part:')
            row.prop_search(data, 'bonepart_name', obj.pose, 'bone_groups', text='')
            row = layout.row(align=True)
            row.prop(data, 'flags_stopatend', text='Stop', toggle=True)
            row.prop(data, 'flags_nomix', text='!Mix', toggle=True)
            row.prop(data, 'flags_syncpart', text='Sync', toggle=True)
            row = layout.row(align=True)
            row.prop(data, 'flags_footsteps', text='Foot Steps', toggle=True)
            row.prop(data, 'flags_movexform', text='Move XForm', toggle=True)
            row = layout.row(align=True)
            row.prop(data, 'flags_idle', text='Idle', toggle=True)
            row.prop(data, 'flags_weaponbone', text='Weapon Bone', toggle=True)
        layout.context_pointer_set(OpExportSkl.bl_idname + '.action', action)
        layout.operator(OpExportSkl.bl_idname, icon='EXPORT')
        layout.label(text='Settings:')
        row = layout.row(align=True)
        row.operator(action_utils.XRayCopyActionSettingsOperator.bl_idname)
        row.operator(action_utils.XRayPasteActionSettingsOperator.bl_idname)
