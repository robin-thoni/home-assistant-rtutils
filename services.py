"""Services."""

from __future__ import annotations

import voluptuous as vol

from homeassistant.core import (
    HomeAssistant,
    ServiceCall,
    callback,
    SupportsResponse,
)
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.service import async_register_admin_service

import yaml

from .const import (
    _LOGGER,
    DOMAIN,
    SERVICE_DUMMY,
    SERVICE_LOAD_YAML,
    ATTR_SERVICE_LOAD_YAML_DATA,
    SERVICE_SVG_TO_PNG,
    ATTR_SERVICE_SVG_TO_PNG_SRC,
    ATTR_SERVICE_SVG_TO_PNG_DST,
    ATTR_SERVICE_SVG_TO_PNG_WIDTH,
    ATTR_SERVICE_SVG_TO_PNG_HEIGHT,
)

def dummy(service: ServiceCall) -> None:
    _LOGGER.debug("Dummy service called with data: %s", service.data)


def load_yaml(service: ServiceCall) -> dict:
    data_dict = yaml.safe_load(service.data[ATTR_SERVICE_LOAD_YAML_DATA])
    return data_dict


def svg_to_png(service: ServiceCall) -> None:

    try:
        from cairosvg import svg2png
    except:
        raise HomeAssistantError("CairoSVG is not installed")
    with open(service.data[ATTR_SERVICE_SVG_TO_PNG_SRC], 'rt') as svg_file:
        svg_code = svg_file.read()
    svg2png(
        bytestring=svg_code,
        write_to=service.data[ATTR_SERVICE_SVG_TO_PNG_DST],
        output_width=service.data.get(ATTR_SERVICE_SVG_TO_PNG_WIDTH),
        output_height=service.data.get(ATTR_SERVICE_SVG_TO_PNG_HEIGHT),
    )


@callback
def async_setup_services(hass: HomeAssistant) -> None:
    """Register the services for the rtutils component."""
    async_register_admin_service(
        hass,
        DOMAIN,
        SERVICE_DUMMY,
        dummy,
        schema=vol.Schema(
            {
            }
        ),
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_LOAD_YAML,
        load_yaml,
        schema=vol.Schema(
            {
                vol.Required(ATTR_SERVICE_LOAD_YAML_DATA): cv.string,
            }
        ),
        supports_response=SupportsResponse.ONLY,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_SVG_TO_PNG,
        svg_to_png,
        schema=vol.Schema(
            {
                vol.Required(ATTR_SERVICE_SVG_TO_PNG_SRC): cv.string,
                vol.Required(ATTR_SERVICE_SVG_TO_PNG_DST): cv.string,
                vol.Optional(ATTR_SERVICE_SVG_TO_PNG_WIDTH): cv.positive_int,
                vol.Optional(ATTR_SERVICE_SVG_TO_PNG_HEIGHT): cv.positive_int,
            }
        ),
    )
