"""Config flow for RT Utils."""

from typing import Any

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from .const import DEFAULT_NAME, DOMAIN


class RtutilsFlowHandler(ConfigFlow, domain=DOMAIN):
    """Handle a RT Utils config flow."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle a flow initialized by the user."""

        if user_input is not None:
            return self.async_create_entry(title=DEFAULT_NAME, data=user_input)
        
        return self.async_show_form(step_id="user")
