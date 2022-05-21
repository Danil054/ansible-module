#!/usr/bin/python3

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: fcreate_module

short_description: Create file

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: Create file by "path" var with "content" var

options:
    path:
        description: Path to file
        required: true
        type: str
    content:
        description: Content for file
        required: false
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - danil_054.fcreate_collection.doc_fragment_name

author:
    - Danil054 for Netology
'''

EXAMPLES = r'''
# 
- name: Test create file
  danil_054.fcreate_collection.fcreate_module.my_test:
    path: /var/tmp/file.txt
    content: "Test file content"

'''

RETURN = r'''
'''

from ansible.module_utils.basic import AnsibleModule

import os

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False)
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    var_path = module.params['path']
    var_content = module.params['content']

    var_state = 'bad'

    if os.path.isfile(var_path):
        with open(var_path) as f:
            cont = f.readline()
            if var_content == cont:
                var_state = 'good'
    else:
        var_state = 'bad'

    if var_state == 'bad':
        with open(var_path,'w') as f:
            f.write(var_content)
            result['changed'] = True
            result['message'] = "File created"
    else:
        result['changed'] = False
        result['message'] = "This file exist with this content"

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)

def main():
    run_module()


if __name__ == '__main__':
    main()
