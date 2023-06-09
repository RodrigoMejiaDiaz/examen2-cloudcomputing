# examen2-cloudcomputing

explicación docker-compose.yml:

    version: "3"
    services:
    zookeeper:
        image: confluentinc/cp-zookeeper:latest
        environment:
        ZOOKEEPER_CLIENT_PORT: 2181
        ZOOKEEPER_TICK_TIME: 2000
        networks:
        - my-network

    kafka:
        image: confluentinc/cp-kafka:latest
        depends_on:
        - zookeeper
        ports:
        - "9092:9092"
        environment:
        KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
        KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092
        KAFKA_AUTO_CREATE_TOPICS_ENABLE: "true"
        KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
        networks:
        - my-network

    producer:
        build:
        context: .
        dockerfile: Dockerfile
        depends_on:
        - kafka
        networks:
        - my-network
        command: python producer.py

    networks:
    my-network:

- El servicio zookeeper utiliza la imagen confluentinc/cp-zookeeper:latest para crear un contenedor de ZooKeeper. ZooKeeper es un servicio de coordinación y gestión de configuración utilizado por Kafka.

- El servicio kafka utiliza la imagen confluentinc/cp-kafka:latest para crear un contenedor de Kafka. Dependiendo de ZooKeeper, Kafka proporciona una plataforma de streaming distribuida para la publicación y suscripción de mensajes.

- El servicio kafka expone el puerto 9092 para permitir la comunicación con los clientes Kafka.

explicación producer.py:

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

- Se importa la clase Producer de la biblioteca confluent_kafka. Esta clase proporciona una interfaz para enviar mensajes a un cluster de Kafka.

- Se define el nombre del tópico como "mi-tema".

- Se configuran las propiedades del productor en un diccionario conf. En este caso, se especifica la dirección del bootstrap server de Kafka (bootstrap.servers) como "kafka:9092" y se establece un ID de cliente (client.id) como "producer".

- Se crea una instancia del productor utilizando la configuración proporcionada.

- Se utiliza el método produce() del productor para enviar un mensaje al tópico especificado. En este caso, se envía el mensaje "Hola Mundo" con la propiedad value.

- Se llama al método flush() del productor para esperar a que el mensaje se envíe correctamente antes de continuar. Esto asegura que el mensaje se haya enviado y se haya confirmado por parte de Kafka.

- Se imprime en la consola el mensaje "Mensaje enviado: Hola Mundo" para indicar que el mensaje se ha enviado correctamente.

Construir contenedores:

- docker-compose up -d --build

Verificar que se ha creado el mensaje Hola Mundo en el tópico 'mi-tema':

- docker-compose exec kafka kafka-console-consumer --topic mi-tema --bootstrap-server kafka:9092 --from-beginning
