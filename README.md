For launch\
docker down\
docker up --build\
docker-compose run flask_app flask db upgrade


For new migrate \
docker-compose exec flask_app flask db migrate -m "Create users table"