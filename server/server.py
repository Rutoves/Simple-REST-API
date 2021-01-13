import os

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

orders = [
    {
        'id': 1,
        'product': u'Pencils',
        'price': 100,
        'quantity': 2,
        'client': u'John'
    }
]

@app.route('/api/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders': orders})

@app.route('/api/orders', methods=['POST'])
def create_order():
    if not request.json or not 'product' in request.json or not 'price' in request.json \
            or not 'quantity' in request.json:
        abort(400)
    order = {
        'id': orders[-1]['id'] + 1,
        'product': request.json['product'],
        'price': request.json['price'],
        'quantity': request.json['quantity'],
        'client': request.json.get('client', ""),
    }
    orders.append(order)
    return jsonify({'created_order': order}), 201

@app.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = list(filter(lambda t: t['id'] == order_id, orders))
    if len(order) == 0:
        abort(404)
    return jsonify({'order': order[0]})

@app.route('/api/orders/<int:order_id>', methods=['PATCH'])
def update_task(order_id):
    order = list(filter(lambda t: t['id'] == order_id, orders))
    if len(order) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'product' in request.json and type(request.json['product']) != str:
        abort(400)
    if 'client' in request.json and type(request.json['client']) != str:
        abort(400)
    if 'price' in request.json and type(request.json['price']) != int:
        abort(400)
    if 'quantity' in request.json and type(request.json['quantity']) != int:
        abort(400)
    order[0]['product'] = request.json.get('product', order[0]['product'])
    order[0]['price'] = request.json.get('price', order[0]['price'])
    order[0]['quantity'] = request.json.get('quantity', order[0]['quantity'])
    order[0]['client'] = request.json.get('client', order[0]['client'])
    return jsonify({'order': order[0]}), 201

@app.route('/api/orders/<int:order_id>', methods=['PUT'])
def update_whole_task(order_id):
    order = list(filter(lambda t: t['id'] == order_id, orders))
    if len(order) == 0:
        abort(404)
    if 'product' not in request.json:
        abort(400)
    if 'price' not in request.json:
        abort(400)
    if 'quantity' not in request.json:
        abort(400)
    if 'client' not in request.json:
        abort(400)
    order[0]['product'] = request.json['product']
    order[0]['price'] = request.json['price']
    order[0]['quantity'] = request.json['quantity']
    order[0]['client'] = request.json['client']
    return jsonify({'order': order[0]}), 201


@app.route('/api/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = list(filter(lambda t: t['id'] == order_id, orders))
    if len(order) == 0:
        abort(404)
    orders.remove(order[0])
    return jsonify({'result': True})

@app.route('/api/orders/reset_to_default', methods=['GET'])
def reset_to_default():
    orders.clear()
    orders.append(
        {
            'id': 1,
            'product': u'Pencils',
            'price': 100,
            'quantity': 2,
            'client': u'John'
        }
    )
    return jsonify({'orders': orders})

@app.route('/api/orders', methods=['DELETE'])
def delete_all_orders():
    orders.clear()
    return jsonify({'result': True})




app.run(host='0.0.0.0', port=int(os.environ.get('HSE_HTTP_FLASK_PORT', 80)))
