For launch\
docker-compose down\
docker-compose up --build\
docker-compose run flask_app flask db upgrade


For new migrate \
docker-compose exec flask_app flask db migrate -m "Create users table"