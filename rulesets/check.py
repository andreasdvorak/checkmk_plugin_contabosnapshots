#!/usr/bin/env python3
#
# target directory: ~/local/lib/python3/cmk_addons/plugins/contabosnapshot/rulesets/

"""CheckMK plugin file to create a rule for the check"""

from cmk.rulesets.v1 import Title
from cmk.rulesets.v1.form_specs import \
      DefaultValue, DictElement, Dictionary, Integer, LevelDirection, SimpleLevels
from cmk.rulesets.v1.rule_specs import \
      CheckParameters, HostCondition, Topic

def _parameter_form():
    return Dictionary(
        elements = {
            "numberofsnapshots": DictElement(
                parameter_form = SimpleLevels(
                    title = Title("Number of snapshots"),
                    form_spec_template = Integer(),
                    level_direction = LevelDirection.LOWER,
                    prefill_fixed_levels = DefaultValue(value=(2, 1)),
                ),
                required = True,
            ),
        }
    )

rule_spec_contabosnapshots = CheckParameters(
    name = "contabosnapshots",
    title = Title("Contabo snapshots"),
    topic = Topic.GENERAL,
    parameter_form = _parameter_form,
    condition = HostCondition(),
)
