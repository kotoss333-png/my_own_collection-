# Ansible Collection - my_own_namespace.yandex_cloud_elk

This collection provides a custom Ansible module `my_own_module` and a role `my_own_role` for creating text files on remote hosts.

## Included Content

### Modules
- `my_own_namespace.yandex_cloud_elk.my_own_module` — Creates a text file at the specified `path` with the given `content`.

### Roles
- `my_own_namespace.yandex_cloud_elk.my_own_role` — Single-task role wrapping `my_own_module` with default parameters:
  - `file_path` (default: `/tmp/default_role_file.txt`)
  - `file_content` (default: `Default content from my_own_role`)

## Example Playbook

```yaml
---
- name: Run my_own_role from collection
  hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: my_own_namespace.yandex_cloud_elk.my_own_role
      vars:
        file_path: "/tmp/collection_role_test.txt"
        file_content: "Hello from collection role!"
```
