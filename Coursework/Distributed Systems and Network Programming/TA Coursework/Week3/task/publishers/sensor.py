import json
from datetime import datetime

from pika import BlockingConnection, ConnectionParameters, PlainCredentials
from pika.exchange_type import ExchangeType

RMQ_HOST = 'localhost'
RMQ_USER = 'rabbit'
RMQ_PASS = '1234'
EXCHANGE_NAME = 'amq.topic'
ROUTING_KEY = 'co2.sensor'

if __name__ == '__main__':
    pass