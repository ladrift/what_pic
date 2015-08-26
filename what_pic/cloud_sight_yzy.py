"""This is API for python in use of Cloud Sight api.

CloudImage is object of a request of image description.
Using CloudImage(url=url) to initiate a CloudImage object,
and using CloudImage.result() to get feedback.
"""
import time
import re
import requests

class CloudImage:
    def __init__(self, url=None, file=None, locale='zh-CN', lang='zh-CN'):
        self.req_url = 'https://api.cloudsightapi.com/image_requests/'
        self.resp_url = 'https://api.cloudsightapi.com/image_responses/'
        self.locale = locale
        self.lang = lang

        self.headers = {
        'Authorization' : 'CloudSight amZd_zG32VK-AoSz05JLIA',
        'Host' : 'api.cloudsightapi.com',
        'Origin:' : 'https://cloudsightapi.com'
        }
        self.upload_ok = False
        self._token = None

        self.session = requests.Session()
        self.session.headers.update(self.headers)

        if url:
            self._url(url)
        elif file:
            self._file(file)
        else:
            print('Cloud Image init failed.')
            self = None

    def _file(self, file):
        """using a file of locale image to initiate.
        """
        self.data = {
                'image_request[locale]': self.locale,
                'image_request[language]': self.lang,
                }
        self.files = {
                'image_request[image]': file
                }
        print('Uploading...')
        resp = self.session.post(self.req_url, \
                data=self.data, files=self.files)

        self._token = resp.json().get('token')
        if self._token:
            self.upload_ok = True
        else:
            print('Upload failed.')

    def _url(self, url):
        """using url of image to to initiate.

        args:
            url: a string of url
        """
        self.data = {
                'image_request[remote_image_url]': url,
                'image_request[locale]': self.locale,
                'image_request[language]': self.lang,
                }

        #try:
        print('Uploading...')
        resp = self.session.post(self.req_url, data=self.data)
        #except Exception:
        #    raise ConnectionError('can not upload image.')

        self._token = resp.json().get('token')
        if self._token:
            self.upload_ok = True
        else:
            print('Upload failed.')

    def _result(self):
        """Return the result or None when _token is None

        return: a dict with status and description
        """
        if self._token:
            resp = self.session.get(self.resp_url + self._token)
        else:
            return None

        result = resp.json()
        return dict(status=result.get('status'), description=result.get('name'))

    def result(self, count=50):
        while count > 0:
            count -= 1
            result = self._result()
            if result:
                if result.get('status') == 'completed':
                    return result.get('description')
                else:
                    print('Not completed')
                    time.sleep(2)
            else:
                return None

def main():
    cloud_img = CloudImage(file=open('link.jpeg', 'rb'))
    if cloud_img:
        #count = 50
        #while count > 0:
        #    result = cloud_img._result()
        #    if result:
        #        if result.get('status') == 'completed':
        #            print(result.get('description'))
        #            break
        #        else:
        #            print('Not completed')
        #            time.sleep(2)
        #    else:
        #        print('result is None')
        #    count -= 1
        print(cloud_img.result())
    else:
        print('cloud_img is None')

    #if CloudImage():
    #    print('pass')


if __name__ == '__main__':
    main()
