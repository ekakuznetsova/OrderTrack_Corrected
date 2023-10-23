import configuration
import data
import requests
import pytest
 #Выполняем запрос на создание заказа
def post_new_order(body):
    return requests.post(configuration.URL+configuration.CREATE_ORDER_PATH,
                         json=body)

# Выполняем запрос на получение заказа по трек-номеру
def get_order_by_track():
    return requests.get(configuration.URL + configuration.GET_ORDER_PATH + str(post_new_order(data.order_body).json()['track']))