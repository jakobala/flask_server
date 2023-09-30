import pandas as pd


class Stats:
    # Variables that will be changed when initialising the object
    initial_data = None
    query_arguments = None

    # Default values if not provided in the URL
    separator = ";"
    column = "Krankenhauskosten"

    # Variables that will be modified during the calculations
    statistics = None
    response = None

    def __init__(self, data, arguments):
        """Initialize the object with data and arguments"""

        # Retrieve data and arguments
        self.initial_data = data
        self.query_arguments = arguments

        # Change separators and targeted column if required
        if arguments and arguments.get("sep"):
            self.separator = arguments.get("sep")

        if arguments and arguments.get("column"):
            self.column = arguments.get("column")

    def do_analysis(self):
        """Perform the statistical analysis of the file sent"""
        df = pd.read_csv(self.initial_data, sep=";")

        self.statistics = ""

    def create_json_response(self):
        """Create the json response of calls that are using the Stat object"""
        self.response = ""
