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

        # Reads the data
        df = pd.read_csv(self.initial_data, sep=self.separator)

        # Test that the required columns exist
        if not {"PID", "Zeitindex"}.issubset(df.columns):
            raise ValueError("PID and Zeitindex must be in the uploaded file")
        if not self.column in df.columns:
            raise ValueError(self.column, " must be in the uploaded file")

        # Create subsets according to time and calculate the statistical parameters
        df_sum = df.groupby("Zeitindex").sum()
        df_mean = df.groupby("Zeitindex").mean()

        # Merge the results into a new dataframe
        df_merged = pd.concat(
            [df_mean[self.column], df_sum[self.column]],
            axis=1,
            keys=["Mean", "Sum"],
        )

        self.statistics = df_merged

    def create_json_response(self):
        """Create the json response of calls that are using the Stat object"""
        self.response = self.statistics.to_json()
