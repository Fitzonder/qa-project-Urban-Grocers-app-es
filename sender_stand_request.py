import requests
import configuration
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def get_new_user_token():
    response = post_new_user(data.user_body)
    try:
        response_body = response.json()
    except requests.exceptions.JSONDecodeError:
        response_body = response.text
    if response.status_code != 201 or not isinstance(response_body, dict) or "authToken" not in response_body:
        raise RuntimeError(
            "Failed to create user. "
            f"Status: {response.status_code}, Body: {response_body}"
        )
    return response_body["authToken"]


def post_new_kit(kit_body, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}",
    }
    return requests.post(
        f"{configuration.URL_SERVICE}{configuration.KITS_PATH}",
        json=kit_body,
        headers=headers,
    )
