# examen2-cloudcomputing

Construir contenedores:
- docker-compose up -d --build

Verificar que se ha creado el mensaje Hola Mundo en el tópico 'mi-tema':
- docker-compose exec kafka kafka-console-consumer --topic mi-tema --bootstrap-server kafka:9092 --from-beginning
