import requests
from random import randint
BASE_URL = "https://petstore.swagger.io/v2"


def teste_generate_orderID():
    return randint(1, 10)
def test_create_order():

    order_id = teste_generate_orderID()

    payload = {
        "id": order_id,
        "petId": 1,
        "quantity": 2,
        "shipDate": "2025-07-17T14:00:00.000Z",
        "status": "placed",
        "complete": True 
        } 
    
    #given a purchase made, when it can be consulted by their code and it is placed, then return 200

    post_resp = requests.post(f"{BASE_URL}/store/order", json=payload)
    assert post_resp.status_code == 200
    post_data = post_resp.json()
    assert post_data["id"] == order_id
    assert post_data["status"] == "placed"

    #given a purchase made, when it can be consulted by their code and the quantity matches, then return 200

    get_resp = requests.get(f"{BASE_URL}/store/order/{order_id}")
    assert get_resp.status_code == 200
    get_data = get_resp.json()
    assert get_data["id"] == order_id
    assert get_data["quantity"] == 2

