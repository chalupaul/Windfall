from bottle import route, view
@route('/test')
@view('test/test')
def test():
    return {"name": "Paul"}

