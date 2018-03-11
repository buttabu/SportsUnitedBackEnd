from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class LeagueDivisionViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = LeagueDivisionSerializer

    def get_queryset(self):
        queryset = LeagueDivision.objects.all()
        return queryset

class LeagueViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,) 
    serializer_class = LeagueSerializer

    def get_queryset(self):
        queryset = League.objects.all()
        return queryset

    #create new league
    def create(self, request):
        permission_classes = (IsAuthenticated,)
        authentication_classes = (TokenAuthentication,)
        user = request.user.id
        # soccer = request.data.get('soccer', False)
        data = {
            'user': user,
            'name': request.data.get('name', None),
            'abbrev': request.data.get('abbrev', None),
            'bio': request.data.get('bio', None),
            'league_start': request.data.get('league_start', None),
            'league_end': request.data.get('league_end', None),
            'playoff_start': request.data.get('playoff_start', None),
        }
        serializer = LeagueSerializer(data=data)
        # Check is user exists before creating a league
        if serializer.is_valid() and data['user'] is not None:
            new_data = serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # used for updating 
    def put(self, request):
        user = request.user.id
        league = League.objects.get(id=request.data.get('id',None))
        data = {
            'name': request.data.get('name', None),
            'abbrev': request.data.get('abbrev', None),
            'bio': request.data.get('bio', None),
            'league_start': request.data.get('league_start', None),
            'league_end': request.data.get('league_end', None),
            'playoff_start': request.data.get('playoff_start', None),
        }
        serializer = LeagueSerializer(data=data)
        if serializer.is_valid() and user is not None:
            serializer.update(league, serializer.validated_data)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
