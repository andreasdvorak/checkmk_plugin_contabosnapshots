# CheckMK Plugin Contabo Snapshots
CheckMK special agent plugin to monitor Contabo snapshots

Tested with CheckMK 2.3.0

I followed [Writing you own check plug-ins](https://docs.checkmk.com/master/de/devel_special_agents.html) and the [Guidelines](https://docs.checkmk.com/latest/en/dev_guidelines.html).

## Install from package


# Special Agent Rule

![Special Agent Rule](images/integration_rule.png?raw=true "Special Agent Rule")

Hostname: The name of the host for which snapshots should be given.

# Service

![Service](images/service.png?raw=true "Service")

# Service Details

![Service details](images/service_details.png?raw=true "Services details")

# Configuration
## Configuration of the integration

![Configuration of the integration](images/integration_rule.png?raw=true "Configuration of the integration")

## Service parameter to configure

![Service Parameter](images/service_rule.png?raw=true "Service Parameter")

## Configuration of host properties

![Properties of host](images/properties_of_host.png?raw=true "Properties of host")

# Development

## Pylint
    pylint -d E0401 -d E0611 $(git ls-files '*.py')

## Creation of mkp
Manifest file tmp/check_mk/contabosnapshots.manifest.temp

```
{'author': 'Andreas Dvorak',
 'description': 'Monitoring of Contabo snapshots',
 'download_url': 'https://github.com/andreasdvorak/checkmk_plugin_contabosnapshots',
 'files': {'cmk_addons_plugins': ['contabosnapshots/agent_based/contabosnapshots.py',
                                  'contabosnapshots/libexec/agent_contabosnapshots',
                                  'contabosnapshots/rulesets/special_agent.py',
                                  'contabosnapshots/server_side_calls/special_agent.py']
           },
 'name': 'contabosnapshots',
 'title': 'Contabo snapshots monitoring with special agent plugin',
 'version': '1.0.0',
 'version.min_required': '2.3.0',
 'version.packaged': 'cmk-mkp-tool 0.2.0',
 'version.usable_until': None
}
```

create the package

    mkp package tmp/check_mk/contabosnapshots.manifest.temp

Path to package: var/check_mk/packages_local