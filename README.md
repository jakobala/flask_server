# Flask server
This project is just a programming exercise. It is a flask server with one health endpoint that accepts GET, one stat endpoint that accepts POST of csv file, and one endpoint to visualize data.

# Running the server
The server can be run in two different way, independent from each other. Using usual python commands, or using Docker

## Run the server using Python
Prerequisite: having python and pip installed

The first time running the server, you will need to create a virtual environment and install the dependencies. Make sure beforehands that python and pip are installed on your computer

```BASH
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then, and also the other times, you need to run the server using the following commands:
```BASH
# cd $REPO_DIR 
source venv/bin/activate
python app.py
```

## Run the server using Docker
Prerequisite: having docker installed

You need first to build the docker container with the following command:
```BASH
docker build --tag python-docker .
```

Then you need to run it with the following command
```BASH
docker run -d -p 8080:5000 python-docker
```

When finished, you should stop the container from running. To do so, list the running containers and then use the container id listed to stop it. The name of the container is "python-docker". Here are the commands to do so:
```BASH
# Lists the running containers
docker ps

# Stops the corresponding container
docker stop $container_id
```


# Commands to test the server
```BASH
# cd $REPO_DIR 
curl -X GET http://localhost:8080/health/

#curl -X POST --data-binary "@test.csv" http://localhost:8080/stats/\?column\=$column\&sep\=$separator
curl -X POST --data-binary "@test.csv" http://localhost:8080/stats/\?column\=Krankenhauskosten\&sep\=\;
curl -X POST --data-binary "@test.csv" http://localhost:8080/stats/\?column\=ICD%20E11%20-%20liegt%20vor\&sep\=\;

```