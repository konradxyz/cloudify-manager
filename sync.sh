#!/bin/bash
set -eax
cp cloudify-manager/plugins/windows-agent-installer/windows_agent_installer/__init__.py cloudify.win1/env/lib/python2.7/site-packages/windows_agent_installer/__init__.py
cp cloudify-plugins-common/cloudify/context.py cloudify.win1/env/lib/python2.7/site-packages/cloudify/context.py
cp cloudify-manager/plugins/windows-agent-installer/windows_agent_installer/tasks.py cloudify.win1/env/lib/python2.7/site-packages/windows_agent_installer/tasks.py

service celeryd-win1 restart
