import os

import requests

import json

SERVER_HOST = os.environ.get('HSE_HTTP_TESTS_SERVER_HOST', 'server')
SERVER_PORT = int(os.environ.get('HSE_HTTP_FLASK_PORT', 80))
URL = 'http://' + SERVER_HOST
if SERVER_PORT != 80:
    URL += ':{}'.format(SERVER_PORT)


def test_get_all_orders():
    response = requests.get(URL + '/api/orders')
    ans = json.loads(response.text)
    correct_ans = {'orders': [
        {
        'id': 1,
        'product': u'Pencils',
        'price': 100,
        'quantity': 2,
        'client': u'John'
        }
    ]}
    assert ans == correct_ans
    assert response.status_code == 200

def test_post_new_order():
    order = {
        'product': 'Clay',
        'price': 200,
        'quantity': 1,
        'client': 'Bob',
    }
    response = requests.post(URL + '/api/orders', json=order)
    order_copy = order.copy()
    order_copy['id'] = 2
    correct_ans = {'created_order': order_copy}
    assert response.status_code == 201
    assert json.loads(response.text) == correct_ans
    response = requests.get(URL + '/api/orders')
    ans = json.loads(response.text)
    correct_ans = {'orders': [
        {
            'id': 1,
            'product': u'Pencils',
            'price': 100,
            'quantity': 2,
            'client': 'John'
        },
        order_copy
    ]}
    assert ans == correct_ans
    assert response.status_code == 200

def test_get_order():
    response = requests.get(URL + '/api/orders/2')
    ans = json.loads(response.text)
    correct_ans = {'order':
        {
            'id': 2,
            'product': 'Clay',
            'price': 200,
            'quantity': 1,
            'client': 'Bob',
        }
    }
    assert ans == correct_ans
    assert response.status_code == 200

def test_patch_order():
    order = {
        'product': 'Vox',
        'price': 150
    }
    response = requests.patch(URL + '/api/orders/2', json=order)
    order_copy = order.copy()
    order_copy['id'] = 2
    order_copy['quantity'] = 1
    order_copy['client'] = 'Bob'
    correct_ans = {'order': order_copy}
    assert response.status_code == 201
    assert json.loads(response.text) == correct_ans
    response = requests.get(URL + '/api/orders')
    ans = json.loads(response.text)
    correct_ans = {'orders': [
        {
            'id': 1,
            'product': u'Pencils',
            'price': 100,
            'quantity': 2,
            'client': 'John'
        },
        order_copy
    ]}
    assert ans == correct_ans
    assert response.status_code == 200

def test_put_order():
    order = {
        'product': 'Paper',
        'price': 50,
        'quantity': 4,
        'client': 'Bill',
    }
    response = requests.put(URL + '/api/orders/2', json=order)
    order_copy = order.copy()
    order_copy['id'] = 2
    correct_ans = {'order': order_copy}
    assert response.status_code == 201
    assert json.loads(response.text) == correct_ans
    response = requests.get(URL + '/api/orders')
    ans = json.loads(response.text)
    correct_ans = {'orders': [
        {
            'id': 1,
            'product': u'Pencils',
            'price': 100,
            'quantity': 2,
            'client': 'John'
        },
        order_copy
    ]}
    assert ans == correct_ans
    assert response.status_code == 200

def test_delete_order():
    response = requests.delete(URL + '/api/orders/2')
    assert json.loads(response.text)['result']
    response = requests.get(URL + '/api/orders')
    ans = json.loads(response.text)
    correct_ans = {'orders': [
        {
            'id': 1,
            'product': u'Pencils',
            'price': 100,
            'quantity': 2,
            'client': 'John'
        }
    ]}
    assert ans == correct_ans
    assert response.status_code == 200

def test_reset_to_default():
    response = requests.get(URL + '/api/orders/reset_to_default')
    ans = json.loads(response.text)
    correct_ans = {'orders': [
        {
        'id': 1,
        'product': u'Pencils',
        'price': 100,
        'quantity': 2,
        'client': u'John'
        }
    ]}
    assert ans == correct_ans
    assert response.status_code == 200

def test_delete_all_orders():
    response = requests.delete(URL + '/api/orders')
    assert json.loads(response.text)['result']
    response = requests.get(URL + '/api/orders')
    ans = json.loads(response.text)
    correct_ans = {'orders': []}
    assert ans == correct_ans
    assert response.status_code == 200