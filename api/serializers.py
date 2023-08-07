from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import Post,like

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField( style={'input_type': 'password'},
        write_only=True )
    class Meta:
        model = User
        fields = ['id','username','email','password','password2']
        extra_kwargs = {
            'password': {'write_only': True},  # Make password field write-only (only used during creation/updation)
        }
        
    def create(self, validated_data):
    # Pop the 'password2' field from validated_data as we don't need it to create the user
        password2 = validated_data.pop('password2', None)

        # Validate that 'password' and 'password2' match
        if validated_data.get('password') != password2:
            raise serializers.ValidationError("Passwords do not match.")

        # Create and return the user instance
        return User.objects.create_user(**validated_data)  
        
        
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

        
        
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        # user details are authenticated
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError('Incorrect Credentials')
        else:
            raise serializers.ValidationError('Must include "username" and "password"')
        return data



        
class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Post
        fields=['id','title','description','content','name','like_count']
        

        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=like
        fields=['id','post_id','user_id']
           
        
