# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Enum definitions."""
from enum import Enum


class HttpMethod(Enum):
    """Http methods."""

    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    PATCH = "PATCH"
    DELETE = "DELETE"


class ContextEnum(Enum):
    """Various context in the app."""

    INSPECTION = "Inspection"
    COMPLAINT = "Complaint"
    CASE_FILE = "Casefile"
    ORDER = "Order"


class PermissionEnum(Enum):
    """Enum for Staff User Permissions."""

    VIEWER = "Viewer"
    USER = "User"
    SUPERUSER = "Superuser"
