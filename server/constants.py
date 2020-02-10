#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#  Copyright Kitware Inc.
#
#  Licensed under the Apache License, Version 2.0 ( the "License" );
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
###############################################################################


# Constants representing the setting keys for this plugin
class PluginSettings(object):
    PROVIDERS_ENABLED = 'NCIAuth.providers_enabled'
    IGNORE_REGISTRATION_POLICY = 'NCIAuth.ignore_registration_policy'

    NCI_CLIENT_ID = 'NCIAuth.NCI_client_id'
    NCI_RETURN_URL = 'NCIAuth.NCI_return_url'
    NCI_API_URL = 'NCIAuth.NCI_api_url'
    NCI_LOGIN_URL = 'NCIAuth.NCI_login_url'
    NCI_VALIDATION_URL = 'NCIAuth.NCI_validation_url'