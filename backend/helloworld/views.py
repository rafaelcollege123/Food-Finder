import json
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, GroupSerializer
import requests


def helloWorldView(request):
    #PRACTICE AREA FOR TESTING API REQUEST ETC
    api_key = "INSERT API KEY"
    headers = {
        "Authorization": "Bearer %s" % api_key,
    }
    response = requests.get(
        "https://api.yelp.com/v3/autocomplete?text=del&latitude=37.786882&longitude=-122.399972",
        headers=headers,
    )
    return HttpResponse(response.text)

def nearApi(request):
    #OFFICIAL API CAL ON URL:\near
    API_KEY = "INSERT API KEY"
    HEADERS = {"Authorization": "Bearer %s" % API_KEY,}
    ENDPOINT = "https://api.yelp.com/v3/businesses/search"

    PARAMETERS = {'term': 'food(all)',
                  'limit': 20,
                  'location': '5500UniversityPkwy,SanBernardino,CA92407',
                  'Radius': 10000,
                  }
    response = requests.get(url = ENDPOINT,params = PARAMETERS, headers = HEADERS)
    
    #next goal is to manipulate responses to return url of businesses

    return HttpResponse(response.text)
def userView(request, userId):
    user = get_object_or_404(get_user_model(), pk=userId)
    dictionary = {
        "id": user.username,
        "email": user.email,
    }
    json_object = json.dumps(dictionary, indent=4)
    return HttpResponse(json_object)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
