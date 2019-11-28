from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import NameSerializer

class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        colors = ['RED', 'YELLOW', 'GREEN', 'BLUE']
        return Response({'msg': 'Happy New Year', 'colors': colors})

    def post(self, request, *args, **kwargs):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'Hello {}, Happy New Year!'.format(name)
            return Response({'msg': msg})
        return Response(serializer.errors, status=404)

    def put(self, request, *args, **kwargs):
        return Response({'msg': 'This response from put method'})

    def patch(self, request, *args, **kwargs):
        return Response({'msg': 'This response from patch method'})

    def delete(self, request, *args, **kwargs):
        return Response({'msg': 'This response from delete method'})
 
