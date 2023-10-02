import base64
from io import BytesIO

from matplotlib.figure import Figure
import matplotlib.pyplot as plt


def visualize_file(statistics):
    """
    Creates an image that visualize the data from a csv file that can be preprocessed by stats
    Designed to be shown within a browser
    """
    # Calculate the usual statistics and store it in a dataframe
    statistics.do_analysis()
    df_stats = statistics.statistics

    # Calculate statistics for patients with and without a condition
    df_initial = statistics.read_dataframe

    df_mean_with_disease = (
        df_initial[df_initial["ICD E11 - liegt vor"] == True]
        .groupby("Zeitindex")
        .mean()
    )

    df_mean_without_disease = (
        df_initial[df_initial["ICD E11 - liegt vor"] == False]
        .groupby("Zeitindex")
        .mean()
    )

    # Generate the figure.
    fig = Figure()

    # Set size and labels to the figures and subplots
    fig, axs = plt.subplots(3, figsize=(10, 10))
    axs[0].set_title("Mean costs all patients")
    axs[1].set_title("Sum costs all patients")
    axs[2].set_title("Mean costs patients with and without type 2 diabetes")
    axs[0].set_ylabel("Hospital costs (€)")
    axs[1].set_ylabel("Hospital costs (€)")
    axs[2].set_ylabel("Hospital costs (€)")

    # Plot the data
    axs[0].plot(df_stats[["Mean"]])
    axs[1].plot(df_stats[["Sum"]])
    (line1,) = axs[2].plot(df_mean_with_disease[["Krankenhauskosten"]])
    (line2,) = axs[2].plot(df_mean_without_disease[["Krankenhauskosten"]])

    # Add legend to the last subplot
    axs[2].legend(
        (line1, line2),
        ("with T2DM", "without T2DM"),
        loc="upper right",
        shadow=True,
    )

    # Make sure that there are no overlap between the subplots
    fig.tight_layout()

    # Save figure to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
