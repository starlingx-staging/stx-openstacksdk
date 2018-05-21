# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# Copyright (c) 2016 Wind River Systems, Inc.
#

from openstack.network import network_service
from openstack import resource2 as resource


class ProvidernetType(resource.Resource):
    resource_key = 'providernet_type'
    resources_key = 'providernet_types'
    base_path = '/wrs-provider/providernet-types'
    service = network_service.NetworkService()

    # capabilities
    allow_list = True

    # Properties
    type = resource.Body('type')
    description = resource.Body('description')
