########
# Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

from setuptools import setup

setup(
    name='cloudify-integration-tests',
    version='3.2',
    author='Gigaspaces',
    author_email='cosmo-admin@gigaspaces.com',
    packages=['testenv',
              'testenv.processes',
              'mock_plugins',
              'mock_plugins.cloudmock',
              'mock_plugins.connection_configurer_mock',
              'mock_plugins.context_plugin',
              'mock_plugins.mock_agent_plugin',
              'mock_plugins.plugin_installer',
              'mock_plugins.testmockoperations',
              'mock_plugins.worker_installer',
              'mock_plugins.mock_workflows'],
    description='Cloudify Integration Tests',
    zip_safe=False,
    install_requires=[
        'cloudify-dsl-parser==3.2',
        'cloudify-rest-client==3.2',
        'cloudify-plugins-common==3.2',
        'cloudify-diamond-plugin==1.2',
        'cloudify-script-plugin==1.2',
        'pika==0.9.13',
        'elasticsearch==1.0.0',
        'celery==3.1.17'
    ],
    entry_points={
        'nose.plugins.0.10': [
            'suitesplitter = testenv.suite_splitter:SuiteSplitter',
        ]
    },
)
