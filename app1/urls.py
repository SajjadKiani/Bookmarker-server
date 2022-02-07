from django.urls import path
from .views import CategoryView, Signup, BookmarkView, Logout, UserView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', obtain_auth_token),
    path('logout/', Logout.as_view()),
    path('signup/', Signup.as_view()),
    path('categories/', CategoryView.as_view()),
    path('bookmarks/', BookmarkView.as_view()),
    path('user/', UserView.as_view()),
]
