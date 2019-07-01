#! /usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

strs = ['suck', 'my', 'ball', 'and', 'dick']

channel.queue_declare(queue='hello')
for s in strs:
	channel.basic_publish(exchange='',
	                      routing_key='hello',
	                      body="yo, {}".format(s))
	print(" [x] Sent {}".format(s))
	time.sleep(5)
connection.close()