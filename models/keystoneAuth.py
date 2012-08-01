import requests, json, pprint
from requests.auth import AuthBase

class KeystoneAuth(AuthBase):
    token = ""
    
    def __init__(self, username, password, tenant):
        self.username = username
        self.password = password
        this.tenant = tenant
        
    def __call__(self, r):
        #modify and return request  
        if token=="":
                
            try:

                tenant = ""
                username = ""
                password = ""
                
                ip = ""
                port = ""
                
                url = "http://" + ip + ":" + port + "/v2.0/tokens"
                payload = ' {"auth":{"tenantName": "' + tenant + '", "passwordCredentials":{"username": "' + username + '", "password":"' + password + '"} }} '
                #payload = '{"auth":{"passwordCredentials":{"username": "' + username + '", "password": "' + password + '"}}}'
                headers = {'content-type': 'application/json'}        
                print "Sending: " + payload + "\n"
                r = requests.post(url, data=payload, headers=headers)
                ans = r.text
                ans = ans.replace('"', "'")
                print json.dumps(ans, indent=4)
                
                
            except Exception, e:
                print "Error: %s" % e
                