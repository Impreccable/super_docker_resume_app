This is a web app that allows users to summarize a text.
It uses python, Docker, Flask and the Ollama API


Connection to DB using pgAdmin:

1) log In
2) add new connection
3) General:
    Name = postgres
4) Connection:
    Host = postgresql_container
    Port = 5432
    Database = postgres
    Username = postgres
    Pass = Azerty123!!!


**************************
CREATING NETWORK (useless)
**************************
links:

    - https://medium.com/@augustineozor/understanding-docker-bridge-network-6e499da50f65
    - https://dockerlabs.collabnix.com/networking/A2-bridge-networking.html

1) while docker is running: docker network create my-network


*****************
   API OLLAMA
*****************

1) docker-compose up --build
2) go inside the container: docker exec -it ollama_container /bin/bash
3) inside the container :   ollama pull ollama2 (4Gb)
4) update:                  docker exec -it ollama_container apt-get update
5) pull container:          docker exec -it ollama_container apt-get install -y python3


testing promt:

1) execute container flask
2) curl http://ollama_container:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Why is the sky blue?"
    }'