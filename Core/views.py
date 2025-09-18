from django.shortcuts import render 
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from .models import Patient, HeartRate
from .serializers import UserRegisterSerializer, PatientSerializer, HeartRateSerializer
from .permissions import IsOwnerOrReadOnly

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]



class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        qs = Patient.objects.all()
        name = self.request.query_params.get('name')
        min_age = self.request.query_params.get('min_age')
        max_age = self.request.query_params.get('max_age')
        if name:
            qs = qs.filter(name__icontains=name)
        if min_age:
            qs = qs.filter(age__gte=int(min_age))
        if max_age:
            qs = qs.filter(age__lte=int(max_age))
        return qs

    @action(detail=True, methods=['post'], url_path='heartrate')
    def add_heartrate(self, request, pk=None):
        patient = self.get_object()
        serializer = HeartRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(patient=patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path='heartrate')
    def list_heartrate(self, request, pk=None):
        patient = self.get_object()
        qs = patient.heartrates.all()
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = HeartRateSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = HeartRateSerializer(qs, many=True)
        return Response(serializer.data)
