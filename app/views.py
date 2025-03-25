
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task, User, TaskAssignment
from .serializers import TaskSerializer, TaskAssignmentSerializer,UserSerializer
from rest_framework import status

class CreateUser(APIView):
    def post(self,request):
        try:
            serializer  = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                return Response({"message":"User Created","data": serializer.data,"status": 201},200)
            else:
                errors = serializer.errors  # Get the validation errors
                field_errors = {field: errors[field][0] for field in errors}  # Extract field-wise errors
                
                return Response({
                    "message":"User not created",
                    "errors": field_errors,  # Show errors field-wise
                    "status": 400
                })
        except Exception as e:
            return Response({"error": str(e), "status": 500})


class TaskCreateAPIView(APIView):
    def post(self,request):
        try:
            serializer  = TaskSerializer(data=request.data)
            if serializer.is_valid():
                task = serializer.save()
                return Response({"message":"Task Created","data": serializer.data,"status": 201},200)
            else:
                errors = serializer.errors  # Get the validation errors
                field_errors = {field: errors[field][0] for field in errors}  # Extract field-wise errors
                
                return Response({
                    "message":"User not created",
                    "errors": field_errors,  # Show errors field-wise
                    "status": 400
                })
        except Exception as e:
            return Response({"error": str(e), "status": 500})


class TaskAssignmentAPIView(APIView):
    def post(self, request):
        try:
            
            taskId = request.data.get('taskId')
            if not taskId:
                return Response({"message":"Enter taskId","status": 400},400)
            userIds = request.data.get('userIds')
            if not userIds:
                return Response({"message":"Enter userIds","status": 400},400)
            
            task = Task.objects.get(id=taskId)
            users = User.objects.filter(id__in=userIds)
            if not users:
                return Response({"message":"user not found","status": 403},403)
                
        
            for user in users:
                existing_assignment = TaskAssignment.objects.filter(task=task, user=user).first()
                if existing_assignment:
                   continue
                TaskAssignment.objects.create(task=task, user=user)
            
            return Response({"message": "Task assigned successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e), "status": 500})


class UserTasksAPIView(APIView):
    def get(self, request, userId=None):
        try:
            if not userId:
                return Response({"message":"Enter userId","status": 400},400)
    
            try:
                user = User.objects.get(id=userId)
            except User.DoesNotExist:
                return Response({"message": "User not found", "status": 404}, status=status.HTTP_404_NOT_FOUND)
            if not user:
                return Response({"message":"user not found","status": 403},403)
            tasks = Task.objects.filter(users=user).order_by("-created_at")
            if not tasks:
                return Response({"message":"user has not assign any task","status": 200},200)
        
            serializer = TaskSerializer(tasks, many=True)
            return Response({"message":"User Asign Task", "data": serializer.data,"status":200},200)
        except Exception as e:
            return Response({"error": str(e), "status": 500})


