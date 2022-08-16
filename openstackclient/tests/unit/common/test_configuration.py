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

from unittest import mock

from openstackclient.common import configuration
from openstackclient.tests.unit import fakes
from openstackclient.tests.unit import utils


class TestConfiguration(utils.TestCommand):

    columns = (
        'auth.password',
        'auth.token',
        'auth.username',
        'identity_api_version',
        'password',
        'region',
        'token',
    )

    columns_unmask = (
        'auth.password',
        'auth.token',
        'auth.username',
        'identity_api_version',
        'region',
    )

    datalist = (
        configuration.REDACTED,
        configuration.REDACTED,
        fakes.USERNAME,
        fakes.VERSION,
        configuration.REDACTED,
        fakes.REGION_NAME,
        configuration.REDACTED,
    )

    opts = [mock.Mock(secret=True, dest="password"),
            mock.Mock(secret=True, dest="token")]

    @mock.patch("keystoneauth1.loading.base.get_plugin_options",
                return_value=opts)
    def test_show(self, m_get_plugin_opts):
        arglist = []
        verifylist = [('mask', True)]
        cmd = configuration.ShowConfiguration(self.app, None)
        parsed_args = self.check_parser(cmd, arglist, verifylist)

        columns, data = cmd.take_action(parsed_args)

        self.assertEqual(self.columns, columns)
        self.assertEqual(self.datalist, data)

    @mock.patch("keystoneauth1.loading.base.get_plugin_options",
                return_value=opts)
    def test_show_unmask(self, m_get_plugin_opts):
        arglist = ['--unmask']
        verifylist = [('mask', False)]
        cmd = configuration.ShowConfiguration(self.app, None)
        parsed_args = self.check_parser(cmd, arglist, verifylist)

        columns_unmask, data = cmd.take_action(parsed_args)

        # TODO: 테스트 케이스 오류 잡기
        # list_columns = list(columns)
        # list_columns.remove('password')
        # list_columns.remove('token')
        # columns = tuple(list_columns)

        self.assertEqual(self.columns_unmask, columns_unmask)
        datalist = (
            fakes.PASSWORD,
            fakes.AUTH_TOKEN,
            fakes.USERNAME,
            fakes.VERSION,
            fakes.REGION_NAME,
        )
        self.assertEqual(datalist, data)

    @mock.patch("keystoneauth1.loading.base.get_plugin_options",
                return_value=opts)
    def test_show_mask(self, m_get_plugin_opts):
        arglist = ['--mask']
        verifylist = [('mask', True)]
        cmd = configuration.ShowConfiguration(self.app, None)
        parsed_args = self.check_parser(cmd, arglist, verifylist)

        columns, data = cmd.take_action(parsed_args)

        self.assertEqual(self.columns, columns)
        self.assertEqual(self.datalist, data)
