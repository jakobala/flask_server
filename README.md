# Flask server
This project is just a programming exercise. It is a flask server with one health endpoint that accepts GET, one stat endpoint that accepts POST of csv file, and one endpoint to visualize data.

# Run the server using Python
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
python flask_server.py
```

# Run the server using Docker




# Commands to test the server
```BASH
# cd $REPO_DIR 
curl -X GET http://localhost:8080/health/
curl -X POST --data-binary "@test.csv" http://localhost:8080/stats/\?column\=$column\&sep\=$separator
curl -X POST --data-binary "@test.csv" http://localhost:8080/stats/\?column\=Krankenhauskosten\&sep\=\;
```