from logging.config import dictConfig
from flask import Flask, request
from functions.general import (
    retrieve_datastream_from_curl,
    retrieve_arguments_from_curl,
    retrieve_datastream_from_default_file,
)
from functions.visualisation import visualize_file
from objects.stats import Stats
from variables.default_variables import debug_mode

app = Flask(__name__)
app.debug = debug_mode

# Configuration of the logging
dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "flask.log",
                "formatter": "default",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["console", "file"]},
    }
)


# API routes
@app.route("/")
def api_root():
    # Log system
    app.logger.info("Query details: %s , %s", request.url, request.method)

    return "This is the root of the api"


@app.route("/health/", methods=["GET"])
def health():
    """This endpoint allows GET and only returns OK"""
    # Log system
    app.logger.info("Query details: %s , %s", request.url, request.method)

    return "OK\n"


@app.route("/stats/", methods=["POST"])
def stats():
    """
    This endpoint allows POST and consume CSV files with at least PID and Zeitindex columns.
    The outcome is a JSON including Sum and Mean grouped by Zeitindex.
    The user can specify the arguments column and sep in the URL
    Column will be the column that is statistically analyzed
    Sep is the separators of the csv file
    If there are spaces in the name of the column, the user should replace them by %20 in the URL
    """

    # Log system
    app.logger.info("Query details: %s , %s", request.url, request.method)

    # Retrieve and analyse the file
    file_to_analyse = retrieve_datastream_from_curl(request)
    arguments = retrieve_arguments_from_curl(request)

    statistics = Stats(file_to_analyse, arguments)
    statistics.do_analysis()
    statistics.create_json_response()
    return statistics.response


@app.route("/visualisation/", methods=["GET", "POST"])
def visualisation():
    """
    This endpoint allows GET and POST
    GET makes a visualisation of the test.csv document
    POST accepts a file as parameter and makes a visualisation of this file
    """
    # Log system
    app.logger.info("Query details: %s , %s", request.url, request.method)

    if request.method == "POST":
        file_to_analyse = retrieve_datastream_from_curl(request)
        arguments = retrieve_arguments_from_curl(request)
    else:
        file_to_analyse = retrieve_datastream_from_default_file()
        arguments = None

    statistics = Stats(file_to_analyse, arguments)

    response = visualize_file(statistics)

    return response


# Running the app
if __name__ == "__main__":
    app.run(host="localhost", port=8080)
