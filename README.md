# CheckMK Plugin Contabo Snapshots
CheckMK special agent plugin to monitor Contabo snapshots

Tested with CheckMK 2.3.0

I followed [Writing you own check plug-ins](https://docs.checkmk.com/master/de/devel_special_agents.html) and the [Guidelines](https://docs.checkmk.com/latest/en/dev_guidelines.html).

## Install from package


# Special Agent Rule

![Special Agent Rule](images/integration_rule.png?raw=true "Special Agent Rule")

# Service

![Service](images/service.png?raw=true "Service")

# Service Details

![Service details](images/service_details.png?raw=true "Services details")

## Service parameter to configure

![Service Parameter](images/service_rule.png?raw=true "Service Parameter")

# Development

## Pylint
    pylint -d E0401 -d E0611 $(git ls-files '*.py')

## Creation of mkp
