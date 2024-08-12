"""Service to call epic.authorize endpoints."""

import requests
from flask import current_app, g

from compliance_api.exceptions import BusinessError
from compliance_api.utils.enum import HttpMethod

from .auth_user_schema import AuthUserSchema
from .constant import API_REQUEST_TIMEOUT


class AuthService:
    """Handle service request for epic.authorize."""

    @staticmethod
    def get_epic_user_by_id(auth_user_id: str):
        """Return the user representation from epic.authorize."""
        auth_user_response_json = _request_auth_service(f"/users/{auth_user_id}")
        return AuthUserSchema().load(auth_user_response_json)

    @staticmethod
    def update_user_group(auth_user_id: str, payload: dict):
        """Update the group of the user in the identity server."""
        update_group_response = _request_auth_service(
            f"/users/{auth_user_id}/group", HttpMethod.PATCH, payload
        )
        return update_group_response


def _request_auth_service(
    self, relative_url, http_method: HttpMethod = HttpMethod.GET, data=None
):
    """REST Api call to authorize service."""
    token = getattr(g, "access_token", None)
    if not token:
        raise BusinessError("No access token found", 401)
    auth_base_url = current_app.config["AUTH_BASE_URL"]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    url = f"{auth_base_url}/{relative_url}"

    if http_method == HttpMethod.GET:
        response = requests.get(url, headers=headers, timeout=API_REQUEST_TIMEOUT)
    elif http_method == HttpMethod.PUT:
        response = requests.put(
            url, headers=headers, data=data, timeout=API_REQUEST_TIMEOUT
        )
    elif http_method == HttpMethod.DELETE:
        response = requests.delete(url, headers=headers, timeout=API_REQUEST_TIMEOUT)
    else:
        raise ValueError("Invalid HTTP method")
    response.raise_for_status()
    return response
