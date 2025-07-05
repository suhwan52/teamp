from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Fixture
from .serializers import FixtureSerializer

class FixtureCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # 인증 필요

    def post(self, request):
        serializer = FixtureSerializer(data=request.data)
        if serializer.is_valid():
            fixture = serializer.save()
            return Response({
                "itemId": fixture.id,
                "name": fixture.name,
                "price": fixture.price,
                "count": fixture.count
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
