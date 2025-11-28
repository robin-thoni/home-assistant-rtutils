"""Services."""

from __future__ import annotations

import voluptuous as vol

from homeassistant.core import HomeAssistant, ServiceCall, callback
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.service import async_register_admin_service

from .const import (
    _LOGGER,
    DOMAIN,
    SERVICE_DUMMY,
)

def dummy(service: ServiceCall) -> None:
    _LOGGER.debug("Dummy service called with data: %s", service.data)


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
