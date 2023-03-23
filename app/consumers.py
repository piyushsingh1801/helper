import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from app.models import Profile
from django.core import serializers
from asgiref.sync import sync_to_async,async_to_sync
# from django.contrib.auth.models import User


class PersonalChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def find_my_id(self):
        print("in call ++++++++++++++++++")
        sender_profile = Profile.objects.filter(phone_number=self.scope['cookies']['user'])
        serialized_queryset = serializers.serialize('json', sender_profile)
        dict_queryset = json.loads(serialized_queryset)
        final_queryset = []
        for i in dict_queryset:
            final_queryset.append(i['fields'])
        for i in final_queryset:
            my_id = i['user']
        print(my_id,"find id====================")
        return my_id
    async def connect(self):
        try:
            my_id = await self.find_my_id()
            other_user_id = self.scope['url_route']['kwargs']['id']
            if int(my_id) > int(other_user_id):
                self.room_name = f'{my_id}-{other_user_id}'
            else:
                self.room_name = f'{other_user_id}-{my_id}' 
            self.room_group_name = 'chat_%s' % self.room_name
            print(self.room_group_name,self.room_name,"??????????????????")
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name,
            )
            await self.accept()
            # await self.send(text_data=self.room_group_name)
        except:
            print("here-----------------------------------")

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print(data)
        message = data['message']
        username = data['username']
        receiver = data['receiver']

        # await self.save_message(username, self.room_group_name, message, receiver)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # @database_sync_to_async
    # def save_message(self, username, thread_name, message, receiver):
    #     ChatModel.objects.create(
    #         sender=username, message=message, thread_name=thread_name)
        