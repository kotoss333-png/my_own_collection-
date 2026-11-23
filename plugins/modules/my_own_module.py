#!/usr/bin/python

# Copyright: (c) 2026, Student <student@example.com>
# GNU General Public License v3.0+ (see COPYING or https://gnu.org)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Creates a text file with specified content

version_added: "1.0.0"

description:
    - This module creates a text file on a remote host at the specified path with the given content.

options:
    path:
        description: Path to the file to be created.
        required: true
        type: str
    content:
        description: Content to write into the file.
        required: false
        type: str
        default: ""

author:
    - Student (@student)
'''

EXAMPLES = r'''
- name: Create a file with hello world
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/test.txt
    content: "Hello, world!"
'''

RETURN = r'''
path:
    description: The path to the created/modified file.
    type: str
    returned: always
    sample: '/tmp/test.txt'
content:
    description: The content written to the file.
    type: str
    returned: always
    sample: 'Hello, world!'
'''

import os
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False, default='')
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    result['path'] = path
    result['content'] = content

    file_exists = os.path.exists(path)
    current_content = None

    if file_exists:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                current_content = f.read()
        except Exception as e:
            module.fail_json(msg=f"Failed to read existing file: {str(e)}", **result)

    if not file_exists or current_content != content:
        result['changed'] = True

        if module.check_mode:
            module.exit_json(**result)

        try:
            dir_name = os.path.dirname(path)
            if dir_name and not os.path.exists(dir_name):
                os.makedirs(dir_name)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            module.fail_json(msg=f"Failed to write file: {str(e)}", **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
