import requests, json
from requests.auth import AuthBase

class KeystoneAuth(AuthBase):
    token = ""
    
    def __init__(self, user):
        self.username = username
        self.password = password
        self.tenant = tenant
        
    def __call__(self, r):
        #modify and return request
        tenant = "MyTenant"
        username = "myuser"
        password = "mypassword"
        
        ip = "198.101.225.234"
        port = "35357"
        
        url = ip + ":" + port
        payload = ' {"auth":{"tenantName": "' + tenant + '", "passwordCredentials":{"username": "' + username + '", "password":"' + password + '"} }} '
        headers = {'content-type': 'application/json'}        
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        
        