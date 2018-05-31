#!/usr/bin/env python3
from ciscoconfparse import CiscoConfParse
from sys import argv

def standardize_intfs(parse):

    ## Search all switch interfaces and modify them
    #
    # r'^interface.+?thernet' is a regular expression, for ethernet intfs
    for intf in parse.find_objects(r'^interface.+?thernet'):

        has_stormcontrol = intf.has_child_with(r' storm-control broadcast')
        is_switchport_access = intf.has_child_with(r'switchport mode access')
        is_switchport_trunk = intf.has_child_with(r'switchport mode trunk')
        has_switchport_negotiate = intf.has_child_with(r'nonegotiate')
        ## Add missing features
        if is_switchport_access and (not has_stormcontrol):
            intf.append_to_family(' storm-control action trap')
            intf.append_to_family(' storm-control broadcast level 0.4 0.3')


        ## Search for these settings on an interface
        elif is_switchport_trunk or has_switchport_negotiate:
            #use two if statement to only remove the oone it finds
            if is_switchport_trunk:
                intf.delete_children_matching('port-security')

            if has_switchport_negotiate:
                intf.delete_children_matching('negotiate')

## Parse the config
parse = CiscoConfParse('ios_audit.conf') # this is our input file

## Search and standardize the interfaces...
standardize_intfs(parse)
parse.commit()     # commit() **must** be called before searching again


## regular expression usage in has_line_with() to find if the config has a matching line
if not parse.has_line_with(r'^service\stimestamp'):
    ## prepend_line() adds a line at the top of the configuration
    parse.prepend_line('service timestamps debug datetime msec localtime show-timezone')
    parse.prepend_line('service timestamps log datetime msec localtime show-timezone')

#Add name to the top of the file
if not parse.has_line_with(r'^config by: '):
    user = argv[1]
    parse.prepend_line('Config by: ' + str(user))


## Write the new configuration
parse.save_as('ios_audit.conf.new2')