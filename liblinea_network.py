class Network:
    @staticmethod
    def ping(url):
        import os
        os.system(f'ping {url}')

    @staticmethod
    def get(url):
        import requests
        response = requests.get(url)
        return response.text
    
    @staticmethod
    def post(url, data):
        import requests
        response = requests.post(url, data=data)
        return response.text
    
    @staticmethod
    def put(url, data):
        import requests
        response = requests.put(url, data=data)
        return response.text
    
    @staticmethod
    def delete(url):
        import requests
        response = requests.delete(url)
        return response.text