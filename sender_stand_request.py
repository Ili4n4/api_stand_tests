import configuration
import requests

import data

def get_docs():
    return requests.get("https://cnt-1254abc5-092c-4ac5-a2eb-649e85979f58.containerhub.tripleten-services.com" + "/docs/")


def get_logs(number_of_params):
    return requests.get("https://cnt-1254abc5-092c-4ac5-a2eb-649e85979f58.containerhub.tripleten-services.com" + "/api/logs/main/",
                        params={"count" : number_of_params})


def post_products_kits(products_ids):
    return requests.post("https://cnt-1254abc5-092c-4ac5-a2eb-649e85979f58.containerhub.tripleten-services.com" + "/api/v1/products/kits/",
                         json = products_ids,
                         headers= data.headers)

response = post_products_kits(data.product_ids)
print(response.status_code)
print(response.json())


def post_new_user(body):
    return requests.post("https://cnt-1254abc5-092c-4ac5-a2eb-649e85979f58.containerhub.tripleten-services.com" + "/api/v1/users/",
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)


def get_users_table():
    return requests.get("https://cnt-cf9d66cc-8860-41ff-bb85-8a60dd2f310f.containerhub.tripleten-services.com" + "/api/db/resources/user_model.csv")  # URL completa del servicio


def positive_assert(param):
    pass


def test_create_user_15_letter_in_first_name_get_success_response():
    return  positive_assert("Aaaaaaaaaaaaaaa")


def negative_assert_symbol(first_name=None):
    return first_name


def negative_assert_no_firstname(param):
    pass


def test_create_user_no_first_name_get_error_response():
    return negative_assert_no_firstname("")



