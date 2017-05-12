def wsgi_application(environ, start_response):
    params = environ["QUERY_STRING"]
    data = str.join("\n",params.split("&")) + "\n"
    status = "200 OK"
    response_headers = [
        ("Content-type", "text/plain"),
        ("Content-lenght", str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data.encode("utf-8")]) #data.encode("utf-8")
