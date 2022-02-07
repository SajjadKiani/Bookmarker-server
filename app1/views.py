from django.contrib.auth.models import User
from django.core import serializers
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Bookmarks
from .serializers import UserSerializer

import urllib.request
from bs4 import BeautifulSoup


def parser(my_url):
    answer = {}

    webUrl = urllib.request.urlopen(my_url)

    data = webUrl.read()

    soup = BeautifulSoup(data, 'lxml')

    try:
        link = soup.head.find('link', attrs={'rel': 'icon'})

        temp = ''

        if (link['href'].startswith('http') == False):
            if (link['href'].startswith('/') == False):
                temp = my_url + '/' + link['href']
            else:
                temp = my_url + link['href']
        else:
            temp = link['href']

        answer.update({'favicon': temp})

    except:
        answer.update({'favicon': ''})

    try:
        des = soup.head.find('meta', attrs={'name': 'description'})
        answer.update({'description': des['content']})
    except:
        answer.update({'description': ''})

    try:
        img = soup.head.find('meta', attrs={'property': 'og:image'})
        answer.update({"image": img['content']})
    except:
        answer.update({"image": ''})

    try:
        title = soup.head.find('title')
        answer.update({"title": title.text})
    except:
        answer.update({"title": ''})

    return answer


class Signup(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        try:
            user = User.objects.create(username=request.data['username'], email=request.data['email'])
            user.set_password(request.data['password'])
            user.save()
            return Response({
                'message': 'success'
            }, status=200)
        except Exception as _:
            return Response({
                'message': 'bad request'
            }, status=400)

class Logout(APIView):

    def post(self, request, **kwargs):
        request.user.auth_token.delete()
        return Response(data=
                'logout'
            ,status=200)

class CategoryView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        return Response(data=[
            cat.name for cat in Category.objects.all()
        ], status=200)

    def post(self, request, **kwargs):
        Category.objects.create(name=request.data['name'], user=request.user)
        return Response(data={
            'message': 'success'
        }, status=200)

class UserView (APIView):
    permission_classes = (IsAuthenticated,)

    def get(self , request, **kwargs):
        return Response (data=
            serializers.serialize('json', User.objects.filter(username=request.user))
        ,status=200)


class BookmarkView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        return Response(data=
                        serializers.serialize('json', Bookmarks.objects.filter(user=request.user))
                        , status=200)

    def post(self, request, **kwargs):

        try:
            html_data = parser(str(request.data['url']))

            bookmark = Bookmarks.objects.create(title=html_data.get('title'), url=request.data['url'],
                                    category=request.data['category'],
                                    description=html_data.get('description'),
                                    favicon=html_data.get('favicon'),
                                    image=html_data.get('image'),
                                    user=request.user)

            return Response(data={
                'title': bookmark.title,
                'url': bookmark.url,
                'description': bookmark.description,
                'category': bookmark.category,
                'favicon': bookmark.favicon,
                'image': bookmark.image,
            }, status=200)

        except:
            return Response (data='htmlParser Error!',status=500)


