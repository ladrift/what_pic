"""This is a module transform a picture to description.
"""
import urllib, urllib.parse
import http.client
import time
import json
import re

class CloudImage(object):
    '''Comment'''
    def __init__(self,imageAddress):
        self.imageAddress = imageAddress
        self.conn = http.client.HTTPConnection('api.cloudsightapi.com')
        self.tokenValue = None

    def _get_token(self,resRead):
        resp = json.loads(resRead)
        return resp['token']

    def _inspect_msg(self, str_msg):
        msg = json.loads(str_msg)
        return msg['status'] == 'completed', msg.get('name')

    def _image_post(self):
        reqData = urllib.parse.urlencode({"image_request[remote_image_url]": self.imageAddress,
            "image_request[locale]":"zh-CN",
            "image_request[language]":"zh-CN"
            })
        reqHeadersPost = {"Accept":"*/*",
            "Accept-Encoding":"gzip,deflate,sdch",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Authorization":"CloudSight amZd_zG32VK-AoSz05JLIA",
            "Connection":"keep-alive",
            "Content-Length":len(reqData),
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Host":"api.cloudsightapi.com",
            "Origin":"http://cloudsightapi.com",
            "Referer":"http://cloudsightapi.com/api",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36",
            }
        self.conn.request('POST', '/image_requests', reqData, reqHeadersPost)
        print('Uploading...')
        res = self.conn.getresponse()
        if res.status == 200:
            print('200:Succeed In Upload')
            return self._get_token(res.read().decode('utf-8'))
        else:
            print('Error:Fail In Upload')
            return False

    def _image_get(self):
        reqHeadersGet={"Accept":"*/*",
            "Accept-Encoding":"gzip,deflate,sdch",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Authorization":"CloudSight amZd_zG32VK-AoSz05JLIA",
            "Connection":"keep-alive",
            "Host":"api.cloudsightapi.com",
            "If-None-Match":"911b902b3cab7b40d24c7f76b4179ff0",
            "Origin":"http://cloudsightapi.com",
            "Referer":"http://cloudsightapi.com/api",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36"
            }
        UrlRequest = ''.join(['/image_responses/', self.tokenValue])
        while True:
            self.conn.request('GET',UrlRequest,'',reqHeadersGet)
            res = self.conn.getresponse()
            if res.status == 200:
                print('200:Succeed')
                resMessage = res.read().decode('utf-8')
                completed, content = self._inspect_msg(resMessage)

                if completed:
                    print('Completed Now!')
                    return content
                else:
                    print('Not Completed')
            else:
                print('Error:Fail')
                return None
            time.sleep(2)

    def run(self):
        self.tokenValue = self._image_post()
        if self.tokenValue:
            return self._image_get()

def validate_url(url):
    regex = re.compile(r"""(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))""")
    if regex.findall(url):
        return True
    else:
        return False

def cloud_sight(url):
    if validate_url(url):
        cloud_img = CloudImage(url)
        result = cloud_img.run()
        return result

if __name__ == "__main__":
    while True:
        testImageUrl = input("请输入图片地址：")
        testCloudImage = CloudImage(testImageUrl)
        result = testCloudImage.run()
        print('description:', result)
