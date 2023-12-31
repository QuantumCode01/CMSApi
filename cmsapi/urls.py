"""cmsapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
# router=DefaultRouter()
# router.register('user',views.UserAPIViewSet,basename='userdetails')
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",include(router.urls)),
    path('api/gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/refreshtoken/', TokenRefreshView.as_view(),name='token_refresh'),
    path('api/verifytoken/', TokenVerifyView.as_view(),name='token_verify'),
    path('api/user/', views.UserAPIView.as_view(),name='user'),
    path('api/user/<str:pk>/',views.UserModificationAPIView.as_view(),name='user'),
    path('api/login/',views.UserLoginAPIView.as_view(),name='userlogin'),
    path('api/check_logged_in/',views.YourView.as_view(), name='check_logged_in'),
    path('api/post/',views.PostListCreateAPIView.as_view(), name='post'),
    path('api/post/<str:pk>/',views.PostRetrieveUpdateDestroyAPIView.as_view(), name='postmodify'),
    path('api/likepost/',views.LikePostView.as_view(), name='likepost'),
    path('api/likepost/<str:pk>/',views.LikeRetrieveUpdateDestroyAPIView.as_view(), name='likepostview'),
    path('api-auth/', include('rest_framework.urls')),
]
