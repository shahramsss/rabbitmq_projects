from multiprocessing import connection
import pika 

connection = pika.BlockingConnection(parameters= pika.ConnectionParameters('localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='logs' , exchange_type='fanout')

result = ch.queue_declare(queue='' , exclusive=True)

q_name = result.method.queue

ch.queue_bind(exchange='logs' , queue=q_name)

def callback(ch , method , properties , body):
    print(f'Recived {body}')

ch.basic_consume(queue=q_name , on_message_callback=callback , auto_ack=True)

ch.start_consuming()