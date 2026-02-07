import data
import sender_stand_request

def positive_assert(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_kit(kit_body, auth_token)

    assert response.status_code == 201
    response_body = response.json()
    assert response_body["name"] == kit_body["name"]

def negative_assert(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_kit(kit_body, auth_token)

    assert response.status_code == 400

def test_create_kit_name_with_one_character():
    kit_body = {"name": "a"}
    positive_assert(kit_body)


def test_create_kit_name_with_511_characters():
    kit_body = {
        "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
    positive_assert(kit_body)


def test_create_kit_name_with_zero_characters():
    kit_body = {"name": ""}
    negative_assert(kit_body)


def test_create_kit_name_with_512_characters():
    kit_body = {
        "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
    negative_assert(kit_body)


def test_create_kit_name_with_special_characters():
    kit_body = {"name": "№%@"}
    positive_assert(kit_body)


def test_create_kit_name_with_spaces():
    kit_body = {"name": " A Aaa "}
    positive_assert(kit_body)


def test_create_kit_name_with_numbers():
    kit_body = {"name": "123"}
    positive_assert(kit_body)


def test_create_kit_name_without_name_parameter():
    kit_body = {}
    negative_assert(kit_body)


def test_create_kit_name_with_number_type():
    kit_body = {"name": 123}
    negative_assert(kit_body)
