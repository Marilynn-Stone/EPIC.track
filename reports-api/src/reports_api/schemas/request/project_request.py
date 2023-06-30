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
"""Project resource's input validations"""
from marshmallow import fields, validate

from .base import RequestBodyParameterSchema, RequestPathParameterSchema, RequestQueryParameterSchema


class ProjectBodyParameterSchema(RequestBodyParameterSchema):
    """Project request body schema"""

    name = fields.Str(
        description="Name of project",
        validate=validate.Length(max=150),
        required=True,
    )
    latitude = fields.Str(
        description="Latitude of project location",
        validate=validate.Length(max=150),
        required=True,
    )
    longitude = fields.Str(
        description="Longitude of project location",
        validate=validate.Length(max=150),
        required=True,
    )

    capital_investment = fields.Int(
        description="Capital investment of project",
        validate=validate.Range(min=0),
        allow_none=True,
        default=None,
    )
    epic_guid = fields.Str(
        description="EPIC GUID of project",
        validate=validate.Length(max=150),
        allow_none=True,
        default=None,
    )
    ea_certificate = fields.Str(
        description="EA Certificate # of project",
        validate=validate.Length(max=150),
        allow_none=True,
        default=None,
    )
    abbreviation = fields.Str(
        description="Abbreviation of the project",
        validate=validate.Length(max=150),
        allow_none=True,
        default=None,
    )
    description = fields.Str(
        description="Description of project",
        validate=validate.Length(max=2000),
        required=True,
    )
    address = fields.Str(
        description="Location description of project",
        validate=validate.Length(max=2000),
        allow_none=True,
        default=None,
    )

    proponent_id = fields.Int(
        description="Proponent id of the project",
        validate=validate.Range(min=1),
        required=True
    )

    type_id = fields.Int(
        description="Type id of the project",
        validate=validate.Range(min=1),
        required=True
    )

    sub_type_id = fields.Int(
        description="SubType id of the project",
        validate=validate.Range(min=1),
        required=True
    )

    region_id_env = fields.Int(
        description="ENV Region id of the project",
        validate=validate.Range(min=1),
        required=True
    )
    region_id_flnro = fields.Int(
        description="NRS Region id of the project",
        validate=validate.Range(min=1),
        required=True
    )

    is_active = fields.Bool(description="Active state of the project")
    is_project_closed = fields.Bool(description="Closed state of the project", default=False)


class ProjectExistenceQueryParamSchema(RequestQueryParameterSchema):
    """Project existence check query parameters"""

    name = fields.Str(
        description='Name of the project',
        validate=validate.Length(max=150),
        required=True
    )

    project_id = fields.Int(
        description='The id of the project',
        validate=validate.Range(min=1),
        missing=None
    )


class ProjectIdPathParameterSchema(RequestPathParameterSchema):
    """project id path parameter schema"""

    project_id = fields.Int(
        description='The id of the project',
        validate=validate.Range(min=1),
        required=True
    )