# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        # self.room_group_name = 'chat_%s' % self.room_name
        rooms = ['g1', 'g2', 'g3', 'g4']

        # Join room group
        for room in rooms:
            await self.channel_layer.group_add(
                room,
                self.channel_name
            )
        await self.accept()
        await self.send("Hello World!")

    async def disconnect(self, close_code):
        # Leave room group
        rooms = ['g1', 'g2', 'g3', 'g4']
        for room in rooms:
            await self.channel_layer.group_discard(
                room,
                self.channel_name
            )

    # Receive message from WebSocket
    async def receive(self, text_data):
        print('receive', text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        room = text_data_json['room']

        # Send message to room group
        await self.channel_layer.group_send(
            room,
            {
                'type': 'chat_message',
                'message': message,
                'room': room
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        print('chat_message', event)
        message = event['message']
        room = event['room']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'room': room
        }))
