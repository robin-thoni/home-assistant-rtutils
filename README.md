# RT Utils

## Requirements

### `svg_to_png` action

The `svg_to_png` action requires a system package installation, which can not be performed via a standard custom component. So we have to trick by checking and, if required, installing the package each time HA starts, so it'll "survive" updates.

Please note:
- Internet access is required each time HA restarts after an upgrade
- There's gonna be a short time (~5 seconds) during which the package will be installing. The action will throw an error if called during that time.

`/config/on_ha_start.sh` (Make it executable `chmod +x /config/on_ha_start.sh`)
```shell
#!/usr/bin/env bash

echo "Running ${0} ${@}"

if ! apk -e info cairo >/dev/null 2>&1
then
    apk add cairo
fi
```

`/config/configuration.yaml`
```yaml
shell_command:
  on_ha_start: /config/on_ha_start.sh
```

Automation:
```yaml
alias: "[Action] On HA Start"
description: ""
triggers:
  - trigger: homeassistant
    event: start
conditions: []
actions:
  - action: shell_command.on_ha_start
    metadata: {}
    data: {}
mode: single
```