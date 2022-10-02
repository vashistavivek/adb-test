from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os
from pymongo import MongoClient

mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
db = MongoClient(mongo_uri)['test_db']

class TodoListView(APIView):

    def get(self, request):
        # db['todos'].delete_many({})
        todos = db['todos'].find()
        todos_list = [todo['todo'] for todo in todos]
        return Response({'data': todos_list, 'msg': 'OK'}, status=status.HTTP_200_OK)
        
    def post(self, request):
        todo = request.POST.get('todo')
        if not todo:
            return Response({'msg': 'Todo must not be empty.'}, status=status.HTTP_400_BAD_REQUEST)
        
        todo_dict = {"todo": todo, 'created_at': datetime.now()}
        db['todos'].insert_one(todo_dict)
        return Response({'msg': 'TODO created successfully.'}, status=status.HTTP_200_OK)

