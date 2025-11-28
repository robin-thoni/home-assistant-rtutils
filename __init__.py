from __future__ import annotations


from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .services import async_setup_services

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Setup RT Utils."""

    async_setup_services(hass)

    return True
