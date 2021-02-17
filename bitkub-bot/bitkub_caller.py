import requests 

URL_API = 'https://api.bitkub.com'

class url_caller:
    def __init__(self, url):
        self.url_api = url

    def get_obj(self, param = None):
        try:
            r = requests.get(url = self.url_api + '/api/status')
            response = r.json()
            return response
        except Exception as e:
            print(e)