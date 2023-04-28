from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


#class CustomUserSerializer(serializers.ModelSerializer):
    #email = serializers.EmailField(required=True)
    #password = serializers.CharField(min_length=8, write_only=True)

    #class Meta:
        #model = StockUser
        #fields = ('email', 'password')
        #extra_kwargs = {'password': {'write_only': True}}

    #def create(self, validated_date):
        #password = validated_date.pop('password', None)
        #instance = self.Meta.model(**validated_date)
        #if password is not None:
            #instance.set_password(password)
        #instance.save
        #return instance



class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=StockUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = StockUser
        fields = ('email', 'password', 'password2')
        extra_kwargs = {
            'password': { 'write_only' : True },
            'password2': { 'write_only' : True }
        }


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs



    def create(self, validated_data):
        user = StockUser.objects.create(
            email=validated_data['email'],
        )

        user.set_password(validated_data['password', 'password2' ])
        user.save()

        return user