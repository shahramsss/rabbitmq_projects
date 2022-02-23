
import pika

connection = pika.BlockingConnection(parameters=pika.ConnectionParameters('localhost'))

ch = connection.channel()

ch.queue_declare(queue= 'first' , durable=True)

message = 'this is a testing message'

ch.basic_publish(exchange='' ,routing_key='first' , body=message , properties=pika.BasicProperties(delivery_mode=2 , headers={'name':'sss'}))
print('Message sent')

connection.close()
