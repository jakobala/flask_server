# Flask server
This project is just a programming exercise. It is a flask server with two endpoints and one accepts a csv in a certain format

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
python3 manage.py runserver
```

# Run the server using Docker