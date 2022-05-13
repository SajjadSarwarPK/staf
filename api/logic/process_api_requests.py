import requests


class ApiTesting:

    def __init__(self):
        self.check = ''
        self.response = ''

    def api_call(self, str_url):
        try:
            payload = {}
            headers = {}
            self.response = requests.request("GET", str_url, headers=headers, data=payload)
            print(self.response.text)
            if self.response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(e)

    def very_response_code(self):
        if self.response.status_code == 200:
            return True
        else:
            return False


    def verify_data(self, str_keyword):
        if str_keyword in self.response.text:
            print("Now verifying === " + str_keyword)
            return True
        else:
            return False