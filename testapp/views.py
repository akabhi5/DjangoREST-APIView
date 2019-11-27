from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        colors = ['RED', 'YELLOW', 'GREEN', 'BLUE']
        return Response({'msg': 'Happy New Year', 'colors': colors})
