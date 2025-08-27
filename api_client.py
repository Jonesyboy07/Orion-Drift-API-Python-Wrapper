import requests

BASE_URL = "https://a2-station-api-prod-708695367983.us-central1.run.app"
HEADER_VAR = "x-api-key"

def get_v1_users(api_key, include_roles=None, include_permissions=None, page_size=None, page=None, search_string=None, last_login=None):
    """List All Users Legacy"""
    url = f"{BASE_URL}/v1/users"
    params = {k: v for k, v in {"include_roles": include_roles, "include_permissions": include_permissions, "page_size": page_size, "page": page, "search_string": search_string, "last_login": last_login}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_users(api_key, data=None):
    """Create Or Update User"""
    url = f"{BASE_URL}/v1/users"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_users(api_key, include_roles=None, include_permissions=None, page_size=None, page=None, search_string=None, last_login=None):
    """List All Users"""
    url = f"{BASE_URL}/v2/users"
    params = {k: v for k, v in {"include_roles": include_roles, "include_permissions": include_permissions, "page_size": page_size, "page": page, "search_string": search_string, "last_login": last_login}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_users(api_key, data=None):
    """Create Or Update User Legacy"""
    url = f"{BASE_URL}/users"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def patch_v1_users_by_accept_tos(api_key, user_id):
    """Update User Tos"""
    url = f"{BASE_URL}/v1/users/{user_id}/accept_tos"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.patch(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_users_by(api_key, user_id):
    """Delete User Legacy"""
    url = f"{BASE_URL}/users/{user_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_v1_users_by(api_key, user_id):
    """Delete User"""
    url = f"{BASE_URL}/v1/users/{user_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_users_by(api_key, user_id, include_roles=None, include_permissions=None, include_bans=None):
    """Get User Legacy"""
    url = f"{BASE_URL}/v1/users/{user_id}"
    params = {k: v for k, v in {"include_roles": include_roles, "include_permissions": include_permissions, "include_bans": include_bans}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_users_by(api_key, user_id, include_roles=None, include_permissions=None, include_bans=None):
    """Get User"""
    url = f"{BASE_URL}/v2/users/{user_id}"
    params = {k: v for k, v in {"include_roles": include_roles, "include_permissions": include_permissions, "include_bans": include_bans}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_users_log_in_server(api_key, data=None):
    """User Server Login Legacy"""
    url = f"{BASE_URL}/users/log_in_server"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_users_log_in_server(api_key, data=None):
    """User Server Login"""
    url = f"{BASE_URL}/v1/users/log_in_server"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_users_log_in_with_key(api_key):
    """Log In With Key Legacy"""
    url = f"{BASE_URL}/users/log_in_with_key"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_users_log_in_with_key(api_key):
    """Log In With Key"""
    url = f"{BASE_URL}/v1/users/log_in_with_key"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_users_log_in(api_key, data=None):
    """User Player Login Legacy"""
    url = f"{BASE_URL}/users/log_in"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_users_log_in(api_key, data=None):
    """User Player Login"""
    url = f"{BASE_URL}/v1/users/log_in"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v2_users_log_in(api_key, data=None):
    """User Player Login V2"""
    url = f"{BASE_URL}/v2/users/log_in"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_users_by_api_key(api_key, user_id):
    """Create User Api Key Legacy"""
    url = f"{BASE_URL}/users/{user_id}/api_key"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_users_by_api_key(api_key, user_id, type=None, data=None):
    """Create User Api Key"""
    url = f"{BASE_URL}/v1/users/{user_id}/api_key"
    params = {k: v for k, v in {"type": type}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_users_by_api_key(api_key, user_id, type=None, include_revoked=None):
    """Get User Api Keys"""
    url = f"{BASE_URL}/v1/users/{user_id}/api_key"
    params = {k: v for k, v in {"type": type, "include_revoked": include_revoked}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def patch_v1_users_by_api_key_by(api_key, user_id, key_id, data=None):
    """Update User Api Key"""
    url = f"{BASE_URL}/v1/users/{user_id}/api_key/{key_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.patch(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_region(api_key):
    """Get User Region"""
    url = f"{BASE_URL}/v1/region"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_user_search(api_key, username=None, limit=None):
    """Get Players By Name"""
    url = f"{BASE_URL}/v1/user_search"
    params = {k: v for k, v in {"username": username, "limit": limit}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_stations_create(api_key, data=None):
    """Create Station Legacy"""
    url = f"{BASE_URL}/stations/create"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_fleets_create(api_key, data=None):
    """Create Fleet"""
    url = f"{BASE_URL}/v1/fleets/create"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_stations_by_config(api_key, station_id):
    """Get Station Config Legacy"""
    url = f"{BASE_URL}/stations/{station_id}/config"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_stations_by_config(api_key, station_id, data=None):
    """Set Station Config Legacy"""
    url = f"{BASE_URL}/stations/{station_id}/config"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_fleets_by_config(api_key, fleet_id):
    """Get Fleet Config"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}/config"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_fleets_by_config(api_key, fleet_id, data=None):
    """Set Fleet Config"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}/config"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_v1_fleets_by_config(api_key, fleet_id, data=None):
    """Delete Fleet Config"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}/config"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v3_fleets_by_online(api_key, fleet_id):
    """Get Fleet Online V2"""
    url = f"{BASE_URL}/v3/fleets/{fleet_id}/online"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_stations_by_user_roles(api_key, station_id, data=None):
    """Add Station User Role By Name Legacy"""
    url = f"{BASE_URL}/v1/stations/{station_id}/user_roles"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v2_fleets_by_user_roles(api_key, fleet_id, data=None):
    """Add Fleet User Role By Name"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/user_roles"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_stations_by_users_by_roles_by(api_key, station_id, user_id, role_id):
    """Add Station User Role Legacy"""
    url = f"{BASE_URL}/stations/{station_id}/users/{user_id}/roles/{role_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_fleets_by_users_by_roles_by(api_key, fleet_id, user_id, role_id):
    """Add a role to a user in a fleet"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}/users/{user_id}/roles/{role_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_stations_by_users_by_role_by(api_key, station_id, user_id, role_id):
    """Delete Station User Role Legacy"""
    url = f"{BASE_URL}/stations/{station_id}/users/{user_id}/role/{role_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_v1_fleets_by_users_by_role_by(api_key, fleet_id, user_id, role_id):
    """Delete Fleet User Role"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}/users/{user_id}/role/{role_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_stations_by_users(api_key, station_id, include_roles=None, include_permissions=None, page_size=None, page=None, search_string=None):
    """Get All Users In Station Legacy"""
    url = f"{BASE_URL}/v1/stations/{station_id}/users"
    params = {k: v for k, v in {"include_roles": include_roles, "include_permissions": include_permissions, "page_size": page_size, "page": page, "search_string": search_string}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_fleets_by_users(api_key, fleet_id, include_roles=None, include_permissions=None, page_size=None, page=None, search_string=None):
    """Get All Users In Fleet"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/users"
    params = {k: v for k, v in {"include_roles": include_roles, "include_permissions": include_permissions, "page_size": page_size, "page": page, "search_string": search_string}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_stations_by_users_by_roles(api_key, station_id, user_id):
    """Get Station User Roles Legacy"""
    url = f"{BASE_URL}/stations/{station_id}/users/{user_id}/roles"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_fleets_by_users_by_roles(api_key, fleet_id, user_id):
    """Get Fleet User Roles"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}/users/{user_id}/roles"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_stations_by_roles(api_key, station_id):
    """Get Station Roles Legacy"""
    url = f"{BASE_URL}/stations/{station_id}/roles"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_stations_by_roles(api_key, station_id, data=None):
    """Create Role Legacy"""
    url = f"{BASE_URL}/stations/{station_id}/roles"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_fleets_by_roles(api_key, fleet_id):
    """Get Fleet Roles"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}/roles"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_fleets_by_roles(api_key, fleet_id, data=None):
    """Create Role"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}/roles"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_stations_by_roles_by(api_key, station_id, role_id):
    """Delete Role Legacy"""
    url = f"{BASE_URL}/stations/{station_id}/roles/{role_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def patch_stations_by_roles_by(api_key, station_id, role_id, data=None):
    """Update Station Role Legacy"""
    url = f"{BASE_URL}/stations/{station_id}/roles/{role_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.patch(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_v1_fleets_by_roles_by(api_key, fleet_id, role_id):
    """Delete Role"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}/roles/{role_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def patch_v1_fleets_by_roles_by(api_key, fleet_id, role_id, data=None):
    """Update Fleet Role"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}/roles/{role_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.patch(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def patch_stations_by_roles_by_permissions(api_key, station_id, role_id, data=None):
    """Assign Perms Legacy"""
    url = f"{BASE_URL}/stations/{station_id}/roles/{role_id}/permissions"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.patch(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def patch_v1_fleets_by_roles_by_permissions(api_key, fleet_id, role_id, data=None):
    """Assign Perms"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}/roles/{role_id}/permissions"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.patch(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_fleets_by_roles_by_users(api_key, fleet_id, role_id):
    """Get Role Users"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/roles/{role_id}/users"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_stations(api_key, include_config=None, include_deployments=None, include_offline_stations=None, page_size=None, page=None):
    """Fetch All Stations Legacy"""
    url = f"{BASE_URL}/v1/stations"
    params = {k: v for k, v in {"include_config": include_config, "include_deployments": include_deployments, "include_offline_stations": include_offline_stations, "page_size": page_size, "page": page}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_fleets(api_key, include_config=None, include_stations=None, include_offline_fleets=None, page_size=None, page=None):
    """Fetch All Fleets"""
    url = f"{BASE_URL}/v2/fleets"
    params = {k: v for k, v in {"include_config": include_config, "include_stations": include_stations, "include_offline_fleets": include_offline_fleets, "page_size": page_size, "page": page}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def patch_stations_by(api_key, station_id, data=None):
    """Update Station Legacy"""
    url = f"{BASE_URL}/stations/{station_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.patch(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_stations_by(api_key, station_id, include_config=None, include_deployments=None, include_disabled=None, region=None, deployment_cl=None):
    """Get Station Legacy"""
    url = f"{BASE_URL}/stations/{station_id}"
    params = {k: v for k, v in {"include_config": include_config, "include_deployments": include_deployments, "include_disabled": include_disabled, "region": region, "deployment_cl": deployment_cl}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_stations_by(api_key, station_id):
    """Delete Station Legacy"""
    url = f"{BASE_URL}/stations/{station_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def patch_v1_fleets_by(api_key, fleet_id, data=None):
    """Update Fleet"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.patch(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_fleets_by(api_key, fleet_id, include_config=None, include_stations=None, include_disabled=None, region=None, deployment_cl=None):
    """Get Fleet"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}"
    params = {k: v for k, v in {"include_config": include_config, "include_stations": include_stations, "include_disabled": include_disabled, "region": region, "deployment_cl": deployment_cl}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_v1_fleets_by(api_key, fleet_id):
    """Delete Fleet"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_stations_by_server_events(api_key, station_id, page_size=None, page=None, event_type=None):
    """Get Server Events Legacy"""
    url = f"{BASE_URL}/v1/stations/{station_id}/server_events"
    params = {k: v for k, v in {"page_size": page_size, "page": page, "event_type": event_type}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_stations_by_server_events(api_key, station_id, data=None):
    """Add Server Event"""
    url = f"{BASE_URL}/v1/stations/{station_id}/server_events"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_fleets_by_server_events(api_key, fleet_id, page_size=None, page=None, event_type=None):
    """Get Server Events"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/server_events"
    params = {k: v for k, v in {"page_size": page_size, "page": page, "event_type": event_type}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_fleets_player_count(api_key):
    """Get Player Count"""
    url = f"{BASE_URL}/v1/fleets/player_count"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v2_fleets_by_users_by_ban(api_key, fleet_id, user_id, duration=None, data=None):
    """Ban Fleet User Legacy"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/users/{user_id}/ban"
    params = {k: v for k, v in {"duration": duration}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v3_fleets_by_users_by_ban(api_key, fleet_id, user_id, data=None):
    """Ban Fleet User"""
    url = f"{BASE_URL}/v3/fleets/{fleet_id}/users/{user_id}/ban"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def patch_v2_fleets_by_users_by_unban(api_key, fleet_id, user_id):
    """Unban Fleet User"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/users/{user_id}/unban"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.patch(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_fleets_by_bans(api_key, fleet_id, include_revoked=None, include_expired=None):
    """Get Fleet Bans"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/bans"
    params = {k: v for k, v in {"include_revoked": include_revoked, "include_expired": include_expired}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_fleets_by_bans(api_key, fleet_id, data=None):
    """Ban Fleet User By Username"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}/bans"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_stations_by_event(api_key, station_id, title=None, description=None, duration=None, deployment_id=None, start_time=None, public=None, signups_open=None, data=None):
    """Create Station Event Legacy"""
    url = f"{BASE_URL}/v1/stations/{station_id}/event"
    params = {k: v for k, v in {"title": title, "description": description, "duration": duration, "deployment_id": deployment_id, "start_time": start_time, "public": public, "signups_open": signups_open}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v2_fleets_by_event(api_key, fleet_id, title=None, description=None, duration=None, station_id=None, start_time=None, public=None, signups_open=None, event_type=None, event_location=None, recurring=None, schedule=None, data=None):
    """Create Fleet Event"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/event"
    params = {k: v for k, v in {"title": title, "description": description, "duration": duration, "station_id": station_id, "start_time": start_time, "public": public, "signups_open": signups_open, "event_type": event_type, "event_location": event_location, "recurring": recurring, "schedule": schedule}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_stations_by_events(api_key, station_id, get_past_events=None):
    """Get Station Events"""
    url = f"{BASE_URL}/v1/stations/{station_id}/events"
    params = {k: v for k, v in {"get_past_events": get_past_events}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_fleets_by_events(api_key, fleet_id, get_past_events=None, limit=None):
    """Get Fleet Events"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/events"
    params = {k: v for k, v in {"get_past_events": get_past_events, "limit": limit}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_events_by(api_key, event_id):
    """Get Fleet Event"""
    url = f"{BASE_URL}/v2/events/{event_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_v2_fleets_by_event_by(api_key, fleet_id, event_id):
    """Delete Fleet Event"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/event/{event_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def patch_v2_fleets_by_event_by(api_key, fleet_id, event_id, data=None):
    """Update Fleet Event"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/event/{event_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.patch(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v2_fleets_by_event_by_users_by_signup(api_key, fleet_id, event_id, user_id, data=None):
    """Signup Fleet Event"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/event/{event_id}/users/{user_id}/signup"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_fleets_by_event_by_signups(api_key, fleet_id, event_id):
    """Get Fleet Event Signups"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/event/{event_id}/signups"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_v2_fleets_by_event_by_signup(api_key, fleet_id, event_id, signup_id=None):
    """Delete Fleet Event Signup"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/event/{event_id}/signup"
    params = {k: v for k, v in {"signup_id": signup_id}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_fleets_by_event_by_config(api_key, fleet_id, event_id):
    """Get Fleet Event Config"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/event/{event_id}/config"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v2_fleets_by_event_by_config(api_key, fleet_id, event_id, data=None):
    """Set Fleet Event Config"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/event/{event_id}/config"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_v2_fleets_by_event_by_config(api_key, fleet_id, event_id, data=None):
    """Delete Fleet Event Config"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/event/{event_id}/config"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_stations_by_deployments(api_key, station_id, data=None):
    """Create Deployment Legacy"""
    url = f"{BASE_URL}/stations/{station_id}/deployments"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_fleets_by_stations(api_key, fleet_id, data=None):
    """Create Station"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}/stations"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_deployments_by_api_key(api_key, deployment_id):
    """Create Deployment Api Key Legacy"""
    url = f"{BASE_URL}/deployments/{deployment_id}/api_key"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_stations_by_api_key(api_key, station_id):
    """Create Station Api Key"""
    url = f"{BASE_URL}/v1/stations/{station_id}/api_key"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_deployments_by_server_events(api_key, deployment_id, data=None):
    """Add Server Event Legacy"""
    url = f"{BASE_URL}/deployments/{deployment_id}/server_events"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def patch_deployments_by(api_key, deployment_id, data=None):
    """Update Deployment Legacy"""
    url = f"{BASE_URL}/deployments/{deployment_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.patch(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_deployments_by(api_key, deployment_id, disable=None):
    """Delete Deployment Legacy"""
    url = f"{BASE_URL}/deployments/{deployment_id}"
    params = {k: v for k, v in {"disable": disable}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def patch_v1_stations_by(api_key, station_id, data=None):
    """Update Station"""
    url = f"{BASE_URL}/v1/stations/{station_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.patch(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_v1_stations_by(api_key, station_id, disable=None):
    """Delete Station"""
    url = f"{BASE_URL}/v1/stations/{station_id}"
    params = {k: v for k, v in {"disable": disable}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_stations_by_deployments(api_key, station_id, page_size=None, page=None, include_offline=None):
    """Get Station Deployments Legacy"""
    url = f"{BASE_URL}/v1/stations/{station_id}/deployments"
    params = {k: v for k, v in {"page_size": page_size, "page": page, "include_offline": include_offline}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_fleets_by_stations(api_key, fleet_id, page_size=None, page=None, include_offline=None):
    """Get Fleet Stations"""
    url = f"{BASE_URL}/v2/fleets/{fleet_id}/stations"
    params = {k: v for k, v in {"page_size": page_size, "page": page, "include_offline": include_offline}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_deployments_by(api_key, deployment_id, include_deployment_config=None, include_station_config=None):
    """Get Deployment Legacy"""
    url = f"{BASE_URL}/v1/deployments/{deployment_id}"
    params = {k: v for k, v in {"include_deployment_config": include_deployment_config, "include_station_config": include_station_config}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_stations_by(api_key, station_id, include_station_config=None, include_fleet_config=None):
    """Get Station"""
    url = f"{BASE_URL}/v2/stations/{station_id}"
    params = {k: v for k, v in {"include_station_config": include_station_config, "include_fleet_config": include_fleet_config}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_deployments_by_config(api_key, deployment_id, include_station_config=None, include_event_config=None):
    """Get Deployment Config Legacy"""
    url = f"{BASE_URL}/v1/deployments/{deployment_id}/config"
    params = {k: v for k, v in {"include_station_config": include_station_config, "include_event_config": include_event_config}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v1_deployments_by_config(api_key, deployment_id, data=None):
    """Set Deployment Config Legacy"""
    url = f"{BASE_URL}/v1/deployments/{deployment_id}/config"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_v1_deployments_by_config(api_key, deployment_id, data=None):
    """Delete Deployment Config Legacy"""
    url = f"{BASE_URL}/v1/deployments/{deployment_id}/config"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_stations_by_config(api_key, station_id, include_fleet_config=None, include_event_config=None):
    """Get Station Config"""
    url = f"{BASE_URL}/v2/stations/{station_id}/config"
    params = {k: v for k, v in {"include_fleet_config": include_fleet_config, "include_event_config": include_event_config}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def post_v2_stations_by_config(api_key, station_id, data=None):
    """Set Station Config"""
    url = f"{BASE_URL}/v2/stations/{station_id}/config"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.post(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def delete_v2_stations_by_config(api_key, station_id, data=None):
    """Delete Station Config"""
    url = f"{BASE_URL}/v2/stations/{station_id}/config"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.delete(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_deployments_by_server_events(api_key, deployment_id, page_size=None, page=None, event_type=None):
    """Get Deployment Server Events Legacy"""
    url = f"{BASE_URL}/v1/deployments/{deployment_id}/server_events"
    params = {k: v for k, v in {"page_size": page_size, "page": page, "event_type": event_type}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_stations_by_server_events(api_key, station_id, page_size=None, page=None, event_type=None):
    """Get Station Server Events"""
    url = f"{BASE_URL}/v2/stations/{station_id}/server_events"
    params = {k: v for k, v in {"page_size": page_size, "page": page, "event_type": event_type}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v2_stations(api_key, page_size=None, page=None, include_offline=None, include_disabled=None, version=None):
    """List Stations"""
    url = f"{BASE_URL}/v2/stations"
    params = {k: v for k, v in {"page_size": page_size, "page": page, "include_offline": include_offline, "include_disabled": include_disabled, "version": version}.items() if v is not None}
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def get_v1_fleets_by_bans_by(api_key, ban_id, fleet_id):
    """Get Ban"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}/bans/{ban_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()

def patch_v1_fleets_by_bans_by(api_key, ban_id, fleet_id, data=None):
    """Update Ban"""
    url = f"{BASE_URL}/v1/fleets/{fleet_id}/bans/{ban_id}"
    params = None
    headers = {HEADER_VAR: api_key}
    json_data = data
    response = requests.patch(url, headers=headers, params=params, json=json_data)
    response.raise_for_status()
    return response.json()
