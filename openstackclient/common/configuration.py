#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

"""Configuration action implementations"""

from keystoneauth1.loading import base
from osc_lib.command import command

from openstackclient.i18n import _

REDACTED = "<redacted>"


class ShowConfiguration(command.ShowOne):
    _description = _("Display configuration details")

    auth_required = False

    def get_parser(self, prog_name):
        parser = super(ShowConfiguration, self).get_parser(prog_name)
        mask_group = parser.add_mutually_exclusive_group()
        mask_group.add_argument(
            "--mask",
            dest="mask",
            action="store_true",
            default=True,
            help=_("Attempt to mask passwords (default)"),
        )
        mask_group.add_argument(
            "--unmask",
            dest="mask",
            action="store_false",
            help=_("Show password in clear text"),
        )
        return parser

    def take_action(self, parsed_args):

        info = self.app.client_manager.get_configuration()

        # Assume a default secret list in case we do not have an auth_plugin
        secret_opts = ["password", "token"]

        if getattr(self.app.client_manager, "auth_plugin_name", None):
            auth_plg_name = self.app.client_manager.auth_plugin_name
            secret_opts = [
                o.dest for o in base.get_plugin_options(auth_plg_name)
                if o.secret
            ]


        for key, value in info.pop('auth', {}).items(): # items(): 딕셔너리화해서 저장시킴
            # parsed_args: Namespace(columns=[], fit_width=False, formatter='table', mask=True, max_width=0, noindent=False, prefix='', print_empty=False, variables=[])
            # clouds.yml에는 auth.password가 존재해서 if문에 걸림
            if parsed_args.mask and key.lower() in secret_opts:
                value = REDACTED

            # info: {'api_timeout': None, 'verify': True, 'cacert': None, 'cert': None, 'key': None, 'baremetal_status_code_retries': '5', 'baremetal_introspection_status_code_retries': '5', 'image_status_code_retries': '5', 'disable_vendor_agent': {}, 'interface': 'public', 'floating_ip_source': 'neutron', 'image_api_use_tasks': False, 'image_format': 'qcow2', 'message': '', 'network_api_version': '2', 'object_store_api_version': '1', 'secgroup_source': 'neutron', 'status': 'active', 'additional_user_agent': [('osc-lib', '2.6.0')], 'verbose_level': 1, 'deferred_help': False, 'region_name': 'RegionOne', 'default_domain': 'default', 'timing': False, 'auth_url': 'http://125.6.39.42/identity', 'username': 'admin', 'password': 'secret123', 'beta_command': False, 'identity_api_version': '3', 'volume_api_version': '3', 'auth_type': 'password', 'networks': [], 'auth.user_domain_id': 'default', 'auth.project_domain_id': 'default', 'auth.project_name': 'demo'}
            info['auth.' + key] = value

        if parsed_args.mask:
            for auth_type in secret_opts:
                info[auth_type] = REDACTED



        ### 인증방식에 따른 마스킹 처리 -> secret_opts에 어떤게 넘어올지(추가될지) 모르는데 password redacted 처리는 노노
        ### parsed_args를 이용해 info의 인증방식을 마스킹해주자
        # if info['auth_type'] == 'password' or 'token':
        #     info['password'] = REDACTED

        return zip(*sorted(info.items()))
