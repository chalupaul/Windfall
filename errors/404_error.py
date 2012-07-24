from bottle import error
@error(404)
def error404(error):
    return "These aren't the droids you're looking for. You can go about your business. Move along."
