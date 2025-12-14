import logging

_LOGGER = logging.getLogger(__package__)

DOMAIN = "rtutils"
DEFAULT_NAME = "RT Utils"

SERVICE_DUMMY = "dummy"

SERVICE_LOAD_YAML = "load_yaml"

ATTR_SERVICE_LOAD_YAML_DATA = "data"

SERVICE_SVG_TO_PNG = "svg_to_png"

ATTR_SERVICE_SVG_TO_PNG_SRC = "svg_path"
ATTR_SERVICE_SVG_TO_PNG_DST = "png_path"
ATTR_SERVICE_SVG_TO_PNG_WIDTH = "png_width"
ATTR_SERVICE_SVG_TO_PNG_HEIGHT = "png_height"
