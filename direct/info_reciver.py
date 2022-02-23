import pika


connection = pika.BlockingConnection(parameters= pika.ConnectionParameters('localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='direct_logs' , exchange_type='direct')

result = ch.queue_declare(queue='' , exclusive=True)

q_name = result.method.queue

severities = ('info','warning','error')

for severrity in severities:
    ch.queue_bind(exchange='direct_logs' , queue=q_name , routing_key=severrity)

print('Wating for messages')

def callback(ch, method, properties, body):
    print(f'{method.routing_key}, {body}')


ch.basic_consume(queue=q_name , on_message_callback = callback , auto_ack=True)
ch.start_consuming()
