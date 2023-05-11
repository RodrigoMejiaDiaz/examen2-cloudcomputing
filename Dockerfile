FROM python:3.9

# Instala la biblioteca confluent-kafka
RUN pip install confluent-kafka

# Copia el archivo del productor
COPY producer.py /

# Comando para ejecutar el productor
CMD [ "python", "producer.py" ]
