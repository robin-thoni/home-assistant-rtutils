"""Services."""

from __future__ import annotations

import voluptuous as vol

from homeassistant.core import (
    HomeAssistant,
    ServiceCall,
    callback,
    SupportsResponse,
)
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.service import async_register_admin_service

import yaml

from .const import (
    _LOGGER,
    DOMAIN,
    SERVICE_DUMMY,
    SERVICE_LOAD_YAML,
    ATTR_SERVICE_LOAD_YAML_DATA,
)

def dummy(service: ServiceCall) -> None:
    _LOGGER.debug("Dummy service called with data: %s", service.data)


def load_yaml(service: ServiceCall) -> dict:
    data_dict = yaml.safe_load(service.data[ATTR_SERVICE_LOAD_YAML_DATA])
    return data_dict


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
