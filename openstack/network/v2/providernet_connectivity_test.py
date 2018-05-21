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


class ProvidernetConnectivityTest(resource.Resource):
    resource_key = 'providernet_connectivity_test'
    resources_key = 'providernet_connectivity_tests'
    base_path = '/wrs-provider/providernet-connectivity-tests'
    service = network_service.NetworkService()

    # capabilities
    allow_create = True
    allow_list = True

    _query_mapping = resource.QueryParameters(
        'audit_uuid', 'providernet_id', 'host_id', 'segmentation_id'
    )

    # Properties
    status = resource.Body('status')
    segmentation_id = resource.Body('segmentation_id')
    updated_at = resource.Body('updated_at')
    host_name = resource.Body('host_name')
    providernet_id = resource.Body('providernet_id')
    host_id = resource.Body('host_id')
    providernet_name = resource.Body('providernet_name')
    audit_uuid = resource.Body('audit_uuid')
    type = resource.Body('type')
    message = resource.Body('message')
