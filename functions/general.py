from io import StringIO
import io
from variables.default_variables import default_file, file_encoding_format


def retrieve_datastream_from_curl(request):
    """Extracts the data received from the post request"""

    # We cannot use the usual request.files['files'] because the curl sends data as stream not as formular
    # Since we cannot change the curl from --data-binary to -F, we need to use stream.read()
    stream = request.stream.read()

    if stream == b"":
        raise ValueError("A file must be uploaded")

    # The stream contains € signs. This removes them so the column can be considered as numerical afterwards
    stream = stream.replace(b"\x80", b"")

    # We convert the stream to a string that can be read afterwards by pandas
    file_as_string = str(stream, file_encoding_format)
    data = StringIO(file_as_string)

    return data


def retrieve_datastream_from_default_file():
    """Extracts the data received from the default data file"""

    file_content = io.open(
        default_file,
        mode="r",
        encoding=file_encoding_format,
    )

    # The stream contains € signs. This removes them so the column can be considered as numerical afterwards
    file_without_currency = file_content.read().replace("\x80", "")

    # We convert the stream to a string that can be read afterwards by pandas
    data = StringIO(file_without_currency)

    return data


def retrieve_arguments_from_curl(request):
    """Extracts the URL arguments from the curl request"""
    arguments = request.args
    return arguments
