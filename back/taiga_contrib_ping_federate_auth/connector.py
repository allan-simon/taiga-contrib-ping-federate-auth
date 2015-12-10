# Copyright (C) 2015 Allan Simon <allan.simon@supinfo.com>
# Copyright (C) 2014 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014 David Barragán <bameda@dbarragan.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from collections import namedtuple

import requests

from django.conf import settings

from taiga.base.connectors.exceptions import ConnectorBaseException

class PingFederateApiError(ConnectorBaseException):
    pass


######################################################
## Data
######################################################

TARGET_RESOURCE = getattr(settings, "PF_AUTH_TARGET_RESOURCE", None)
SERVICE_URL = getattr(settings, "PF_AUTH_SERVICE_URL", None)
USERNAME = getattr(settings, "PF_AUTH_SERVICE_USERNAME", None)
PASSWORD = getattr(settings, "PF_AUTH_SERVICE_PASSWORD", None)
INSTANCE_ID = getattr(settings, "PF_AUTH_INSTANCE_ID", None)

User = namedtuple(
    "User",
    [
        "guid",
        "username",
        "email",
        "full_name",
        "bio",
    ],
)


######################################################
## utils
######################################################

def _get(url: str, params: dict, headers: dict) -> dict:
    """
    Make a GET call.
    """
    response = requests.get(
        url,
        params=params,
        headers=headers,
    )

    data = response.json()
    if response.status_code != 200:
        raise PingFederateApiError(
            {
                "status_code": response.status_code,
                "error": data.get("error", "")
            },
        )
    return data

######################################################
## Convined calls
######################################################

def call_assertion(reference):

    uri = SERVICE_URL + '/ext/ref/pickup'
    params = {'REF' : reference}
    headers = {
        'ping.uname' : USERNAME,
        'ping.pwd' : PASSWORD,
        'ping.instanceId' : INSTANCE_ID,
    }

    data = _get(uri, params, headers)
    data.get("email", None)

    return User(
        guid=data.get("userGUID", None),
        username=data.get("subject", None),
        full_name=data.get("firstname", None) + " " + data.get("lastname", None),
        email=data.get("email", None),
        bio="",
    )
