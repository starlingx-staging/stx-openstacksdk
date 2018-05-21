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


class ProvidernetNetList(resource.Resource):
    resource_key = 'network'
    resources_key = 'networks'
    base_path = '/wrs-provider/providernets'
    service = network_service.NetworkService()

    default_base_path = '/wrs-provider/providernets/'

    # capabilities
    allow_list = True

    # Properties
    name = resource.Body('name')
    providernet_type = resource.Body('providernet_type')
    segmentation_id = resource.Body('segmentation_id', type=int)
    vxlan = resource.Body('vxlan', type=dict)
    id = resource.Body('id')
    vxlan_id = resource.Body('vxlan_id')
