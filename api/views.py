from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer,UserLoginSerializer,PostSerializer,LikeSerializer
from django.contrib.auth.models import User
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login,logout
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,AllowAny
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from .permissions import IsPostOwnerOrReadOnly



# Create your views here.

# to create refresh and access token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# user details apiview
class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

# get all user details
    def get(self, request,pk=None, format=None):
        data=User.objects.all()
        serializer=UserSerializer(data,many=True)
        return Response(serializer.data)
    
    
# create user by post method   
    def post(self,request,format=None):
        data=request.data
        serializer=UserSerializer(data=data)      #data is passed to serializer
        if serializer.is_valid():
            user=serializer.save()
            # refresh and access token are generated
            token=get_tokens_for_user(user)
            res={'token': token,'msg':'Data Created'}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view for user update, retriev and delete by providing id    
class UserModificationAPIView(RetrieveUpdateDestroyAPIView):  
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset=User.objects.all()
    serializer_class=UserSerializer
    

#User login 
class UserLoginAPIView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # from serializer user data is retrieve and pass it to the RefreshTokenfunction
        refresh = RefreshToken.for_user(user)
        login(request,user)
        access_token = str(refresh.access_token)
        return Response({'msg':'LoggedIn successfully','access_token': access_token})





        
    

# To verify user is logged in or not        
class YourView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(request.user)
            # User is logged in, perform desired actions
            return Response({'message': 'You are logged in.'}, status=status.HTTP_200_OK)
        else:
            # User is not logged in
            return Response({'message': 'You are not logged in.'}, status=status.HTTP_401_UNAUTHORIZED)






# Post create and get all the post details
class PostListCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    # Get method to view all created posts
    def get(self, request, format=None):
        # count the number of times the post is liked and shows with the post details
        data=Post.objects.annotate(like_count=models.Count('like'))
        serializer=PostSerializer(data,many=True)
        return Response(serializer.data)
    
    
# creating post 
    def post(self,request,format=None):
        data=request.data
        serializer=PostSerializer(data=data)
        if serializer.is_valid():
            print(request.user)
            serializer.save(name=request.user)
            res={'msg':'Post Created'}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

# post update,delete and retrieve
class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):  
    # Get the post_id from the request data
    authentication_classes = [JWTAuthentication]
    #Only the user who created the post can put, patch and delete that post.
    permission_classes = [IsAuthenticated,IsPostOwnerOrReadOnly]
    # count the number of likes and shows individuall details
    queryset=Post.objects.annotate(like_count=Count('like'))
    serializer_class=PostSerializer
    
    
    
# to create like for post
class LikePostView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
# show all likes     
    def get(self, request,*args,**kwargs):
        data=like.objects.all()
        serializer=LikeSerializer(data,many=True)
        return Response(serializer.data)
        
    
    
    
# creating or liking a post
    def post(self, request, *args, **kwargs):
        # Get the post_id from the request data
        post_id = request.data.get('post_id')
        
        # Check if the post exists
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Create the like object
        liked_data = {'post_id': post.id, 'user_id': request.user.id}
        serializer = LikeSerializer(data=liked_data)

        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# retrieve, update and delete post   
class LikeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
      # Get the id of likes from the request data
    queryset=like.objects.all()
    serializer_class=LikeSerializer
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    