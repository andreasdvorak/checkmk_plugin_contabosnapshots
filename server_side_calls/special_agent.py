#!/usr/bin/env python3

"""Configuration how to call the special agent"""
# Store in your Checkmk site at:
# ~/local/lib/python3/cmk_addons/plugins/contabosnapshot/server_side_calls/special_agent.py

from cmk.server_side_calls.v1 import noop_parser, SpecialAgentConfig, SpecialAgentCommand

def _agent_arguments(params, host_config):
    args = [
        "--clientid", str(params['clientid']),
        "--clientsecret", params['clientsecret'].unsafe(),
        "--apiuser", params['apiuser'],
        "--apipassword", params['apipassword'].unsafe(),
        "--hostname", params['hostname'],
    ]
    yield SpecialAgentCommand(command_arguments=args)

special_agent_contabosnapshots = SpecialAgentConfig(
    name="contabosnapshots",
    parameter_parser=noop_parser,
    commands_function=_agent_arguments
)
