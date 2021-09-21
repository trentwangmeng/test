# coding:utf-8
# ==============================
#         请求的封装
# ==============================
import requests

class Requests:
    def send_get(self,url,params=None,headers=None):
        if headers == None:
            res = requests.get(url=url, params=params)
        else:
            res = requests.get(url=url, params=params, headers=headers)
        return res

    def send_post(self,url,data,headers=None):
        if headers == None:
            res=requests.post(url=url,data=data)
        else:
            res=requests.post(url=url,data=data,headers=headers)
        return res

    def send_put(self, url, data, headers=None):
        if headers == None:
            res = requests.put(url=url, data=data)
        else:
            res = requests.put(url=url, data=data, headers=headers)
        return res

    def send_delete(self, url, data, headers=None):
        if headers == None:
            res = requests.delete(url=url, data=data)
        else:
            res = requests.delete(url=url, data=data, headers=headers)
        return res

    def send_request(self, method, url, data, headers=None):
        res=None
        if method=='GET':
            res = self.send_get(url=url,params=data, headers=headers)
        elif method=='POST':
            res = self.send_post(url=url,data=data, headers=headers)
        elif method=='PUT':
            res = self.send_put(url=url,data=data, headers=headers)
        elif method=='DELETE':
            res = self.send_delete(url=url,data=data, headers=headers)
        return res

if __name__ == '__main__':
    req = Requests()
    res = req.send_request(method='GET',url="http://www.baidu.com", data="", headers=None)
    print(res.text)
