"""This module contains all operator classes for the addon."""

import bpy

from .build_import_plans import AF_OP_BuildImportPlans
from .connection_status import AF_OP_ConnectionStatus
from .delete_provider_bookmark import AF_OP_DeleteProviderBookmark
from .delete_provider_bookmark_header import AF_OP_DeleteProviderBookmarkHeader
from .execute_import_plan import AF_OP_ExecuteImportPlan
from .initialize_provider import AF_OP_InitializeProvider
from .new_provider_bookmark import AF_OP_NewProviderBookmark
from .new_provider_bookmark_header import AF_OP_NewProviderBookmarkHeader
from .update_asset_list import AF_OP_UpdateAssetList
from .update_implementations_list import AF_OP_UpdateImplementationsList


def register():
    """Registers all operator classes."""
    for cl in registration_targets:
        bpy.utils.register_class(cl)


def unregister():
    """Unregisters all operator classes."""
    for cl in reversed(registration_targets):
        bpy.utils.unregister_class(cl)


# List of classes to be registered for the addon
registration_targets = [
    AF_OP_InitializeProvider,
    AF_OP_UpdateAssetList,
    AF_OP_UpdateImplementationsList,
    AF_OP_BuildImportPlans,
    AF_OP_ExecuteImportPlan,
    AF_OP_ConnectionStatus,
    AF_OP_NewProviderBookmark,
    AF_OP_DeleteProviderBookmark,
    AF_OP_DeleteProviderBookmarkHeader,
    AF_OP_NewProviderBookmarkHeader,
]
