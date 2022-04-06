start:
		docker-compose up

down:
		docker-compose down

re:
		docker-compose up --build

clean:
		docker rm $$(docker ps -qa);
		
cleanvol:
		docker volume rm $$(docker volume ls -q);
		# sudo rm -rf /home/waldis/data/wp/*
		# sudo rm -rf /home/waldis/data/db/*

cleannet:
		docker network rm $$(docker network ls -q);
		
fclean:
		docker rmi $$(docker image ls -q);

