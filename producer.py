from confluent_kafka import Producer

topic = "mi-tema"

# Configura las propiedades del productor
conf = {
    'bootstrap.servers': 'kafka:9092',
    'client.id': 'producer'
}

# Crea una instancia del productor
producer = Producer(conf)

# Envía el mensaje "Hola Mundo" al tema
producer.produce(topic, value="Hola Mundo")

# Espera a que el mensaje se envíe correctamente
producer.flush()

# El mensaje se ha enviado correctamente
print("Mensaje enviado: Hola Mundo")
print("Ejcute el siguiente comando: docker-compose exec kafka kafka-console-consumer --topic mi-tema --bootstrap-server kafka:9092 --from-beginning")
