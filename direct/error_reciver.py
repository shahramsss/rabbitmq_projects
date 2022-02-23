import pika


connection = pika.BlockingConnection(parameters=pika.ConnectionParameters('localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='direct_logs' , exchange_type='direct')

result = ch.queue_declare(queue='' , exclusive=True)

q_name = result.method.queue

severity = 'error'

ch.queue_bind(exchange='direct_logs' , queue=q_name , routing_key=severity)

print('Wating for message')

def callback(ch , method , properties , body):
    with open('error_logs.log' , 'a') as el:
        el.write(str(f'{body}') + '\n')

ch.basic_consume(queue=q_name , on_message_callback=callback, auto_ack=True)

ch.start_consuming()

