from flask import Flask, request
from functions.general import (
    retrieve_datastream_from_curl,
    retrieve_arguments_from_curl,
)

# from functions.stats import analyse_file, create_json_response_for_stats
from objects.stats import Stats

app = Flask(__name__)
app.debug = True
app.config["MAX_CONTENT_LENGTH"] = 160 * 1000 * 1000


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
    This endpoint allows POST and consume CSV files.
    The outcome is an additional column in JSON that includes Sum and Mean.
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
