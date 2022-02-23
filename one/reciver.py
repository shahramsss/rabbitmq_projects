import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

ch2 = connection.channel()

ch2.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(f'Recived {body}')


ch2.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)

print('Waiting for messages. To exit press CTRL+C')
ch2.start_consuming()
