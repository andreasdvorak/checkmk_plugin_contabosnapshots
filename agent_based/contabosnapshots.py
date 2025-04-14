#!/usr/bin/env python3
#
# target directory: ~/local/lib/python3/cmk_addons/plugins/contabosnapshots/agent_based/

"""CheckMK server part of the plugin to create services from the raw data"""

# Example for output from agent
# ---------------------------------------------------------
# <<<contabosnapshots:sep(0)>>>
# snap1742473207;nextcloudupdate;2025-03-20T12:20:07.866Z;2025-04-19T12:20:07.863Z
# snap1742373214;osupdate;2025-03-19T08:33:34.389Z;2025-04-18T08:33:34.388Z

# testing
# cmk -vI --detect-plugins=contabosnapshots <hostname>
# cmk -v[vv] --detect-plugins=contabosnapshots [--debug] <hostname>

from typing import Any, Mapping
from cmk.agent_based.v2 import \
     AgentSection, CheckPlugin, Service, Result, State, DiscoveryResult, CheckResult

Section = Mapping[str, Mapping[str, str]]

def parse_contabosnapshots(string_table) -> dict:
    """parse data from agent check

    Args:
        data (dict): data of snapshots

    Returns:
        parsed: parsed data
    """
    #print(string_table)
    parsed = {}
    for line in string_table:
        parsed[line[0]] = {"name": line[1], "datecreated": line[2], "datedelete": line[3]}
    #print(parsed)
    return parsed

def discovery_contabosnapshots(section: Section) -> DiscoveryResult:
    """discovery of services

    Args:
        section (Section): data

    Returns:
        DiscoveryResult: _description_

    Yields:
        Iterator[DiscoveryResult]: _description_
    """
    yield Service()

def check_contabosnapshots(params, section: Section) -> CheckResult:
    """check the data"""
    number_of_snapshots = len(section)
    print(params)
    for i in params["numberofsnapshots"]:
        if isinstance(i, tuple):
            warn_level, crit_level = i

    if number_of_snapshots < crit_level:
        state = State.CRIT
    elif number_of_snapshots < warn_level:
        state = State.WARN
    else:
        state = State.OK

    yield Result(
        state = state,
        summary = f"Number of snapshots: {number_of_snapshots} \
            (warn:{warn_level}/crit:{crit_level})",
        details = str(section)
    )

agent_section_contabosnapshots = AgentSection(
    name = "contabosnapshots",
    parse_function = parse_contabosnapshots,
)

check_plugin_contabosnapshots = CheckPlugin(
    name = "contabosnapshots",
    service_name = "Contabo snapshots",
    discovery_function = discovery_contabosnapshots,
    check_function = check_contabosnapshots,
    check_default_parameters = {"numberofsnapshots": ("fixed", (2,1))},
    check_ruleset_name = "contabosnapshots",
)
