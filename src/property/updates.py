from enum import Enum
import logging
import bpy

LOGGER = logging.getLogger("af.property.updates")
LOGGER.setLevel(logging.DEBUG)


class AF_VariableQueryUpdateTarget(Enum):
	update_asset_list_parameter = "update_asset_list_parameter"
	update_implementation_list_parameter = "update_implementation_list_parameter"
	update_nothing = "update_nothing"

	@classmethod
	def to_property_enum(cls):
		return list(map(lambda c: (c.value, c.value, c.value), cls))


# General update functions


def update_init_url(property, context):
	LOGGER.debug("update_init_url")
	bpy.ops.af.initialize_provider()

	if bpy.ops.af.update_asset_list.poll():
		bpy.ops.af.update_asset_list()

	if bpy.ops.af.update_implementations_list.poll():
		bpy.ops.af.update_implementations_list()


def update_provider_header(property, context):
	LOGGER.debug("update_provider_header")
	if bpy.ops.af.connection_status.poll():
		bpy.ops.af.connection_status()

	if bpy.ops.af.update_asset_list.poll():
		bpy.ops.af.update_asset_list()

	if bpy.ops.af.update_implementations_list.poll():
		bpy.ops.af.update_implementations_list()


def update_asset_list_index(property, context):
	LOGGER.debug("update_asset_list_index")
	if bpy.ops.af.update_implementations_list.poll():
		bpy.ops.af.update_implementations_list()


def update_implementation_list_index(property, context):
	LOGGER.debug("update_implementation_list_index")


#def update_implementation_list_query(property,context):
#	print("update_implementation_list_query")
#	if bpy.ops.af.update_implementations_list.poll():
#		bpy.ops.af.update_implementations_list()
#
#def update_asset_list_query(property,context):
#	print("update_asset_list_query")
#	if bpy.ops.af.update_asset_list.poll():
#		bpy.ops.af.update_asset_list()

# Update functions for variable query parameters


def update_asset_list_parameter(property, context):
	LOGGER.debug("update_asset_list_parameter")
	if bpy.ops.af.update_asset_list.poll():
		bpy.ops.af.update_asset_list()

	if bpy.ops.af.update_implementations_list.poll():
		bpy.ops.af.update_implementations_list()


def update_implementation_list_parameter(property, context):
	LOGGER.debug("update_implementation_list_parameter")
	if bpy.ops.af.update_implementations_list.poll():
		bpy.ops.af.update_implementations_list()


def update_variable_query_parameter(property, context):
	LOGGER.debug("update_variable_query_parameter")
	if hasattr(property, "update_target"):
		if property.update_target == AF_VariableQueryUpdateTarget.update_implementation_list_parameter.value:
			update_implementation_list_parameter(property, context)
		if property.update_target == AF_VariableQueryUpdateTarget.update_asset_list_parameter.value:
			update_asset_list_parameter(property, context)
	else:
		LOGGER.warn(f"No update_target on {property}")
