from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Patient, HeartRate
from django.utils import timezone

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('id','username','email','password','role')


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Patient
        fields = ('id','name','age','gender','address','created_by','created_at')


    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError('Age must be positive')
        return value


class HeartRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartRate
        fields = ('id','patient','bpm','recorded_at','created_at')
        read_only_fields = ('created_at', 'patient')


    def validate_bpm(self, value):
        if value <= 0 or value > 300:
            raise serializers.ValidationError('bpm must be between 1 and 300')
        return value


    def validate_recorded_at(self, value):
        if value > timezone.now():
            raise serializers.ValidationError('recorded_at cannot be in the future')
        return value