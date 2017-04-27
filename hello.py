def app(env, start_response):
	params = [bytes(i + '\r\n', 'ascii') for i in env['QUERY_STRING'].split('&')]
	body = []
	status = '200 OK'
	headers = [('Content-Type', 'text/plain')]
	start_response(status, headers)
	return body
