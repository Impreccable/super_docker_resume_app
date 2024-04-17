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
   API MISTRAL
*****************

1) deleted container ollama and pulled  mistral one : https://docs.mistral.ai/self-deployment/vllm/
