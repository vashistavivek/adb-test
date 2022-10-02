from .mongo import TodoHandler
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TodoListView(APIView):

    def __init__(self):
        super().__init__()
        self.todo_handler = TodoHandler()

    def get(self, request):
        todos_list = self.todo_handler.get_all_todo()
        return Response({'data': todos_list, 'msg': 'OK', 'success': True}, status=status.HTTP_200_OK)
        
    def post(self, request):
        todo = request.POST.get('todo')
        if not todo:
            return Response({'msg': 'Todo must not be empty.', 'success': False}, status=status.HTTP_400_BAD_REQUEST)
        
        flag = self.todo_handler.add_todo(todo)
        if not flag:
            return Response({'msg': 'TODO creation failed!', 'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'msg': 'TODO created successfully.', 'success': True}, status=status.HTTP_200_OK)

