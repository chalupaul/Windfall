import requests, json, pprint
from requests.auth import AuthBase

class KeystoneService(object):
    
    @staticmethod
    def getToken(self,(user_model) user):
        print ""