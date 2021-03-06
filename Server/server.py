#!/usr/bin/env python3
# coding: utf-8

import json
import uuid

from flask import Flask, request, make_response
import redis

app = Flask(__name__)
redis_conn = redis.StrictRedis()


def bad_request(uuid, message):
    return make_response(json.dumps({'uuid': uuid, 'error': message}), 400)


def not_found(uuid, message='not found'):
    return make_response(json.dumps({'uuid': uuid, 'error': message}), 404)


@app.route('/tx/info/', methods=['POST'])
def add_tx_info():
    data = json.loads(request.data)
    uuid_hex = uuid.uuid4().hex
    chain = data.get('chain')
    if not chain:
        return bad_request('null', 'Invalid chain type')
    expire = int(data.get('expire') or 3600)
    if expire > 3600:
        expire = 3600
    transaction = data.get('transaction')
    if not isinstance(transaction, dict):
        return bad_request('null', 'Invalid transaction data')

    data['uuid'] = uuid_hex
    data['expire'] = expire

    redis_key_info = 'tx:info:{uuid}'.format(uuid=uuid_hex)
    redis_key_status = 'tx:status:{uuid}'.format(uuid=uuid_hex)
    redis_value_info = json.dumps(data)
    redis_value_status = json.dumps({'uuid': uuid_hex, 'status': 'pending'})
    redis_conn.set(redis_key_info, redis_value_info, ex=expire)
    redis_conn.set(redis_key_status, redis_value_status, ex=expire)
    return json.dumps({'uuid': uuid_hex})


@app.route('/tx/info/<uuid>', methods=['GET'])
def get_tx_info(uuid):
    redis_key = 'tx:info:{uuid}'.format(uuid=uuid)
    redis_value = redis_conn.get(redis_key)
    return redis_value or not_found(uuid)


@app.route('/tx/status/<uuid>', methods=['PUT'])
def update_tx_status(uuid):
    redis_key = 'tx:status:{uuid}'.format(uuid=uuid)
    redis_value = redis_conn.get(redis_key)
    if not redis_value:
        return not_found(uuid)
    redis_data = json.loads(redis_value)

    data = json.loads(request.data)
    status = data.get('status')
    error = data.get('error')
    transaction = data.get('transaction')
    if status == 'success':
        if not isinstance(transaction, dict) or 'hash' not in transaction:
            return bad_request(uuid, 'Invalid transaction data(tx_hash)')
    elif status in ['denied', 'faied']:
        if not error:
            return bad_request(uuid, 'Error message is required!')
    else:
        return bad_request(uuid, 'Invalid status')

    redis_data['status'] = status
    redis_data['error'] = error
    redis_data['transaction'] = transaction

    redis_value = json.dumps(redis_data)
    redis_conn.set(redis_key, redis_value)
    return json.dumps({'uuid': uuid})


@app.route('/tx/status/<uuid>', methods=['GET'])
def get_tx_status(uuid):
    redis_key = 'tx:status:{uuid}'.format(uuid=uuid)
    redis_value = redis_conn.get(redis_key)
    return redis_value or not_found(uuid)


@app.after_request
def after_request(resp):
    for header in [
            'Access-Control-Allow-Origin',
            'Access-Control-Allow-Headers',
            'Access-Control-Allow-Methods',
    ]:
        resp.headers[header] = '*'
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
