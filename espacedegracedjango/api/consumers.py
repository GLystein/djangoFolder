# api/consumers.py
import json
# from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from asgiref.sync import async_to_sync
import json
from .models import *

# class MyConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         pass
#
#     async def receive(self, text_data):
#         # Handle incoming messages from React if needed
#         pass
#
#     async def send_update_message(self, event):
#         message = event['message']
#         await self.send(text_data=json.dumps({'message': message}))