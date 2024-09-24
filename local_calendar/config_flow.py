"""Config flow for Local Calendar integration."""

from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.helpers import config_validation as cv
from homeassistant.util import slugify

from .const import CONF_CALENDAR_NAME, CONF_CALENDAR_URL, CONF_STORAGE_KEY, DOMAIN

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_CALENDAR_NAME): str,
        vol.Optional(CONF_CALENDAR_URL): cv.url,
    }
)


class LocalCalendarConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Local Calendar."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        if user_input is None:
            return self.async_show_form(
                step_id="user", data_schema=STEP_USER_DATA_SCHEMA
            )

        key = slugify(user_input[CONF_CALENDAR_NAME])
        self._async_abort_entries_match({CONF_STORAGE_KEY: key})
        user_input[CONF_STORAGE_KEY] = key
        return self.async_create_entry(
            title=user_input[CONF_CALENDAR_NAME], data=user_input
        )
