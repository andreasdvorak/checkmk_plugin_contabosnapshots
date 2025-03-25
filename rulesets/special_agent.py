#!/usr/bin/env python3
#
# Store in your Checkmk site at:
# ~/local/lib/python3/cmk_addons/plugins/contabosnapshot/rulesets/special_agent.py

"""CheckMK plugin file to configure the parameter for the special agent"""

from cmk.rulesets.v1.form_specs import \
    DefaultValue, Dictionary, DictElement, String, Password, migrate_to_password
from cmk.rulesets.v1.rule_specs import \
    SpecialAgent, Topic, Help, Title

def _formspec():
    return Dictionary(
        title=Title("Contabo snaphots"),
        help_text=Help("This rule is to configure special agent to check the Contabo snapshots."),
        elements = {
            "clientid": DictElement(
                required=True,
                parameter_form=String(
                    title=Title("Client ID"),
                    prefill=DefaultValue(""),
                ),
            ),
            "clientsecret": DictElement(
                required=True,
                parameter_form=Password(
                    title=Title("Client secret"),
                    migrate=migrate_to_password,
                ),
            ),
            "apiuser": DictElement(
                required=True,
                parameter_form=String(
                    title=Title("API user"),
                    prefill=DefaultValue(""),
                ),
            ),
            "apipassword": DictElement(
                required=True,
                parameter_form=Password(
                    title=Title("API password"),
                    migrate=migrate_to_password,
                ),
            ),
            "hostname": DictElement(
                required=True,
                parameter_form=String(
                    title=Title("Hostname"),
                    prefill=DefaultValue(""),
                    help_text=Help(
                        "Host for that snapshots should exists. "
                        "Use only hostname not FQDN."
                    )
                ),
            ),
        }
    )

rule_spec_contabosnapshots = SpecialAgent(
    topic=Topic.GENERAL,
    name="contabosnapshots",
    title=Title("Contabo snaphots"),
    parameter_form=_formspec,
)
