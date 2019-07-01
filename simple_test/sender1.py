#! /usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
for i in range(0, 10):
	channel.basic_publish(exchange='',
	                      routing_key='hello',
	                      body="yo, here's " + str(i))
	print(" [x] Sent {}".format(i))
	time.sleep(2)
connection.close()