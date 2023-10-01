from flask import Flask, request
from functions.general import (
    retrieve_datastream_from_curl,
    retrieve_arguments_from_curl,
)

from objects.stats import Stats

app = Flask(__name__)
app.debug = False


@app.route("/")
def api_root():
    return "This is the root of the api"


@app.route("/health/", methods=["GET"])
def health():
    """This endpoint allows GET and only returns OK"""
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

    if request.method == "POST":
        return "Visualisation POST"

    return "Visualisation GET"


if __name__ == "__main__":
    app.run(host="localhost", port=8080)