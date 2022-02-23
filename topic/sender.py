import pika

connection = pika.BlockingConnection(parameters=pika.ConnectionParameters('localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='topic_logs' , exchange_type='topic')

messages ={
    'error.warning.important':'This is an inmportant message',
    'info.debug.notimportant':'This is not an inmportant message',
}


for k,v in messages.items():
    ch.basic_publish(exchange='topic_logs' , routing_key=k , body=v)

print('Sent')

connection.close()