#!/usr/bin/env python
import pika
import sys
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

route_key = 'send2'

strs = ['holly', 'shit', 'Jesus']

for s in strs:
	channel.basic_publish(exchange='direct_logs', routing_key=route_key, body=s)
	print(" [x] Sent route_key %s :%s " % (route_key, s))	
	time.sleep(2)

connection.close()