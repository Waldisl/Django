start:
		docker-compose -f ./docker-compose.yaml up

down:
		docker-compose -f ./docker-compose.yaml down

re:
		docker-compose -f ./docker-compose.yaml up --build

clean:
		docker rm $$(docker ps -qa);
		
cleanvol:
		docker volume rm $$(docker volume ls -q);
		sudo rm -rf /home/waldis/data/wp/*
		sudo rm -rf /home/waldis/data/db/*

cleannet:
		docker network rm $$(docker network ls -q);
		
fclean:
		docker rmi $$(docker image ls -q);

