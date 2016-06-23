from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializer import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404


class UserListAPI(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        serializer_users = serializer.data
        #renderer = JSONRenderer()
        #json_users = renderer.render(serializer_users)
        #return HttpResponse(json_users)
        return Response(serializer_users)

class UserDetailAPI(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)