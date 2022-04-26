import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        self.send(text_data=json.dumps({
            'status': 'connected'
        }))

    def receive(self, text_data):
        try:
            print(text_data)
            text_data_json = json.loads(text_data)
            message = text_data_json['message']

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )
        except:
            pass

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def chat_message(self, event):
        try:
            message = event['message']

            self.send(text_data=json.dumps({
                'type': 'chat',
                'message': message
            }))
        except:
            pass
