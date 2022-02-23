import pika

connection = pika.BlockingConnection(parameters=pika.ConnectionParameters('localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='logs', exchange_type='fanout')

ch.basic_publish(exchange='logs', routing_key='', body='This is testing fanout')

print('Sent message')

ch.close()
