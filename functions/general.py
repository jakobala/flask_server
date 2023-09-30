from io import StringIO


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
    file_as_string = str(stream, "iso-8859-1")
    data = StringIO(file_as_string)

    return data


def retrieve_arguments_from_curl(request):
    """Extracts the URL arguments from the curl request"""
    arguments = request.args
    return arguments
