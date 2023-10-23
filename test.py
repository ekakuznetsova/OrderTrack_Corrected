import configuration
import data
import requests
import pytest
import sender_stand_request

#Кузнецова Екатерина, 9 когорта, финальный проект
# Тест 1. Получение кода 200 на запрос на получение заказа по трек-номеру
def test_get_order_by_track():
    assert sender_stand_request.get_order_by_track().status_code == 200

