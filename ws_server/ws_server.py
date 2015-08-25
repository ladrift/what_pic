import json

from autobahn.asyncio.websocket import WebSocketServerProtocol, \
    WebSocketServerFactory
from cloud_sight_yzy import CloudImage

def dict2bytes(dic, encoding='utf-8'):
    return json.dumps(dic, ensure_ascii=False).encode(encoding)

class WhatPicServerProtocol(WebSocketServerProtocol):

    def sendUploadedMsg(self):
        uploaded = {
                'title': 'response',
                'content': 'uploaded',
                }
        payload = dict2bytes(uploaded)
        self.sendMessage(payload=payload, isBinary = False)

    def sendResultMsg(self, result):
        result_dict = {
                'title': 'result',
                'content': result,
                }
        payload = dict2bytes(result_dict)
        self.sendMessage(payload=payload, isBinary=False)

    def sendMistakeMsg(self):
        mistake = {
                'title': 'response',
                'content': 'mistake',
                }
        payload = dict2bytes(mistake)
        self.sendMessage(payload=payload, isBinary=False)

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary reject")
            return
        else:
            print("Text message received: {0}"\
                    .format(payload.decode('utf8')))
            message = json.loads(payload.decode('utf-8'))
            if message['title'] == 'URL':
                url = message['content']
                cloud_img = CloudImage(url=url)
                if cloud_img:
                    # image uploaded
                    self.sendUploadedMsg()

                    result = cloud_img.result()
                    if result:
                        self.sendResultMsg(result)
                    else:
                        print('result is None')
                        self.sendMistakeMsg()
                else:
                    print('cloud_img is None')
                    self.sendMistakeMsg()


    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))


def start_websock(host='127.0.0.1', port=9000):
    try:
        import asyncio
    except ImportError:
        # Trollius >= 0.3 was renamed
        import trollius as asyncio

    factory = WebSocketServerFactory("ws://127.0.0.1:9000", debug=False)
    factory.protocol = WhatPicServerProtocol

    loop = asyncio.get_event_loop()
    coro = loop.create_server(factory, '0.0.0.0', 9000)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.close()

if __name__ == '__main__':
    start_websock()
