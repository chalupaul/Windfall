from bottle import request, route, view, get, post


@get('/test')
@view('test/test')
def testget():
    return {"name": "John"}

@get('/auth')
def authget(db):
    return "Any non blank api key will work."

@post('/auth')
def auth(db):
    key = request.forms.get('api_key')
    if(key!=""):        
        users = db.query(User)
        if (user==null):
            print "No user"
        else:
            return "Key accepted"
    else:
        return "Key denied"
    

    




