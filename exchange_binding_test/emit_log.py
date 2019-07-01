#!/usr/bin/env python
import pika
import sys
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

strs = ['holly', 'smoke', 'good', 'lord']

for s in strs:
	message = ' '.join(sys.argv[1:]) or "info: {}".format(s)
	channel.basic_publish(exchange='logs', routing_key='', body=message)
	time.sleep(2)
	print(" [x] Sent %r" % message)
connection.close()

print(sys.argv[1:])
