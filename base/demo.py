import requests


class RunMain:

    '''
    def __init__(self, url, method, data=None):
        self.res = self.run_main(url, method, data)
    '''

    def send_get(self,url, data):
        res = requests.get(url=url, params=data)
        return res.json()

    def send_post(self, url, data):
        res = requests.post(url=url, data=data)
        return res.json()

    def run_main(self, url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    url = "http://106.75.9.19:88/topic/topic_list"
    data = {
        'page': 2,
        'pagesize': 3
    }
    run = RunMain()
    res = run.run_main(url, 'GET', data)
    print(res)



