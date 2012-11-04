from bottle import request, route, view, get, post, static_file


@get('/media/:path#.+#')
def server_static(path):
    return static_file(path, root='/opt/windfall/zodiacServer/')
@get('/favicon.ico')
def get_favicon():
    return server_static('favicon.ico')
