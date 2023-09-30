from io import StringIO


def retrieve_datastream_from_curl(request):
    stream = request.stream.read()

    if stream == b"":
        raise ValueError("A file must be uploaded")

    file_as_string = str(stream, "cp437")

    data = StringIO(file_as_string)

    return data


def retrieve_arguments_from_curl(request):
    arguments = request.args
    return arguments
