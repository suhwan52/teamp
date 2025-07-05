from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Fixture
from .serializers import FixtureSerializer
from django.http import Http404

class FixtureCreateView(APIView):
    # permission_classes = [permissions.IsAuthenticated]  #인증

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

class FixtureUpdateView(APIView):    
    def patch(self, request, itemId):
        try:
            fixture = Fixture.objects.get(id=itemId)
        except Fixture.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = FixtureSerializer(fixture, data=request.data, partial=True)
        if serializer.is_valid():
            fixture = serializer.save()
            return Response({
                "itemId": fixture.id,
                "name": fixture.name,
                "price": fixture.price,
                "count": fixture.count
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FixtureDeleteView(APIView):
    def delete(self, request, itemId):
        try:
            fixture = Fixture.objects.get(id=itemId)
        except Fixture.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        fixture.delete()
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    
class FixtureListView(APIView):
    def get(self, request):
        page = int(request.GET.get('page',1))   #쿼리 파라미터 받기
        size = int(request.GET.get('size',10))
        #전체 데이터 쿼리셋
        queryset = Fixture.objects.all().order_by('id')
        total_count = queryset.count()
        total_page = (total_count + size - 1) // size

        #페이징 적용
        start = (page - 1) * size
        end = start + size
        fixtures = queryset[start:end]

        #데이터 직렬화, itemId로 변환
        data = [
            {
                "itemId":obj.id,
                "name": obj.name,
                "price": obj.price,
                "count": obj.count
            }
            for obj in fixtures
        ]
        return Response({
            "page": page,
            "size": size,
            "totalPage": total_page,
            "totalCount": total_count,
            "data": data
        }, status=status.HTTP_200_OK)