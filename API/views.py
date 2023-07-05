from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from .myPagination import MyPageNumberPagination
from .serializers import HomeModelSerializer, ServicesModelSerializer, AboutModelSerializer, DoctorsModelSerializer, \
    BookModelSerializer, ReviewModelSerializer, commentModelSerializer, ContactModelSerializer
from .throttling import DKThrottle
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import viewsets
from .models import HomeModel, ServicesModel, AboutModel, DoctorsModel, BookModel, ReviewModel, commentModel, \
    ContactModel

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


# Create your views here.


class HomeModelViewSet(viewsets.ModelViewSet):
    queryset = HomeModel.objects.all()
    serializer_class = HomeModelSerializer
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle, DKThrottle]
    # filter_backends = [SearchFilter, OrderingFilter]
    # ordering_fields = ['name']
    # Search_fields = ['name']
    # pagination_class = MyPageNumberPagination


class ServicesModelViewSet(viewsets.ModelViewSet):
    queryset = ServicesModel.objects.all()
    serializer_class = ServicesModelSerializer
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle, DKThrottle]
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['ServiceName']
    Search_fields = ['ServiceName']


class AboutModelViewSet(viewsets.ModelViewSet):
    queryset = AboutModel.objects.all()
    serializer_class = AboutModelSerializer
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle, DKThrottle]
    # filter_backends = [SearchFilter, OrderingFilter]
    # ordering_fields = ['name']
    # Search_fields = ['name']


class DoctorsModelViewSet(viewsets.ModelViewSet):
    queryset = DoctorsModel.objects.all()
    serializer_class = DoctorsModelSerializer
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle, DKThrottle]
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['DoctorName']
    Search_fields = ['DoctorName']


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookModelSerializer
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle, DKThrottle]
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['name']
    Search_fields = ['name']


class ReviewModelViewSet(viewsets.ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewModelSerializer
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle, DKThrottle]
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['name']
    Search_fields = ['name']


class commentModelViewSet(viewsets.ModelViewSet):
    queryset = commentModel.objects.all()
    serializer_class = commentModelSerializer
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class ContactModelViewSet(viewsets.ModelViewSet):
    queryset = ContactModel.objects.all()
    serializer_class = ContactModelSerializer
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle, DKThrottle]
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['first_name']
    Search_fields = ['first_name']
