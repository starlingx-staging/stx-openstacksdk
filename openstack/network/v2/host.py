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


class Host(resource.Resource):
    resource_key = 'host'
    resources_key = 'hosts'
    base_path = '/hosts'
    service = network_service.NetworkService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # ignores the id field on creating the resource; send a POST instead
    # of a PUT and do not append the ID to the end of the URL
    # the id field is required by the neutron command
    ignore_id_on_create = True

    # Properties
    subnets = resource.Body('subnets', type=int)
    name = resource.Body('name')
    routers = resource.Body('routers', type=int)
    created_at = resource.Body('created_at')
    updated_at = resource.Body('updated_at')
    availability = resource.Body('availability')
    id = resource.Body('id')
    ports = resource.Body('ports', type=int)
    agents = resource.Body('agents', type=list)
