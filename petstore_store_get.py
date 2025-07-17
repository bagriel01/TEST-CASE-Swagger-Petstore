import requests
from random import randint

BASE_URL = "https://petstore.swagger.io/v2"

#given pet inventories status are registered. when the inventory is consulted, then returns 200

def teste_get_shop_inventory():
    response = requests.get(f"{BASE_URL}/store/inventory")

    assert response.status_code == 200

#given the inventory is consulted, when input is a valid order ID, then returns 200
    
def teste_get_shop_orderID():
    response = requests.get(f"{BASE_URL}/store/order/{randint(1,10)}")

    assert response.status_code == 200
