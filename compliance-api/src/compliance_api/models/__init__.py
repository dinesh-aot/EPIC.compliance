# Copyright © 2024 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This exports all of the models and schemas used by the application."""

from .agency import Agency
from .case_file import CaseFile, CaseFileInitiationOption, CaseFileOfficer
from .db import db, ma, migrate
from .inspection import (
    Inspection, InspectionAttendance, InspectionAttendanceOption, InspectionInitiationOption, InspectionOfficer,
    IRStatusOption, IRTypeOption)
from .position import Position
from .project import Project
from .project_status import ProjectStatusOption
from .staff_user import PERMISSION_MAP, PermissionEnum, StaffUser
