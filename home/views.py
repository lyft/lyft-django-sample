import base64
import json
import datetime
import urllib2

from django.shortcuts import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings

from social.apps.django_app.default.models import UserSocialAuth

ORIGIN_LAT = 37.7749
ORIGIN_LONG = -122.4194

from bravado.client import SwaggerClient

# import logging
#
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

TIMEOUT = 30

def login(request):
    
    context = {"request": request}
    return render_to_response('login.html', context, context_instance=RequestContext(request))

@login_required
def home(request):

    api, options = get_lyft(request.user)
    response = None

    profile = api.User.get_profile(_request_options=options).result(timeout=TIMEOUT)

    context = {"request": request, 'response': response, 'profile': profile}
    return render_to_response('home.html', context, context_instance=RequestContext(request))

@login_required
def availability(request):
    api, options = get_lyft(request.user)
    response = None

    drivers = api.Public.get_drivers(lat=ORIGIN_LAT, lng=ORIGIN_LONG, _request_options=options).result(timeout=TIMEOUT)

    context = {'request': request, 'response': response, 'settings': settings, 'location': {'lat': ORIGIN_LAT, 'long': ORIGIN_LONG}, 'drivers': drivers}
    return render_to_response('availability.html', context, context_instance=RequestContext(request))

@login_required
def request(request):

    api, options = get_lyft(request.user)

    eta = api.Public.get_eta(lat=ORIGIN_LAT, lng=ORIGIN_LONG, ride_type='lyft', _request_options=options).result(timeout=TIMEOUT)
    types = api.Public.get_ridetypes(lat=ORIGIN_LAT, lng=ORIGIN_LONG, _request_options=options).result(timeout=TIMEOUT)

    response = None

    if request.method == 'POST':
        type = request.POST.get('type')

        lat = request.POST.get('o_lat')
        lng = request.POST.get('o_lng')
        origin = {'lat':lat, 'lng':lng}

        lat = request.POST.get('d_lat')
        lng = request.POST.get('d_lng')
        destination = {'lat':lat, 'lng':lng}

        ride_request = {'ride_type': type, 'origin': origin, 'destination': destination}
        try:
            response = api.User.post_rides(request=ride_request, _request_options=options).result(timeout=TIMEOUT)
        except Exception as e:
            response = e
        print response

    context = {'request': request, 'response': response, 'eta': eta, 'types': types}
    return render_to_response('request.html', context, context_instance=RequestContext(request))

@login_required
def rides(request):

    api, options = get_lyft(request.user)
    response = None

    start_time = datetime.datetime.now() - datetime.timedelta(days=90)
    rides = api.User.get_rides(start_time=start_time, _request_options=options).result(timeout=TIMEOUT)

    context = {'request': request, 'response': response, 'rides': rides}
    return render_to_response('rides.html', context, context_instance=RequestContext(request))

from django.contrib.auth import logout as auth_logout
def logout(request):
    
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')

def get_lyft(user):

    # Header: "Authorization: Bearer <access_token>"
    social = user.social_auth.get(provider='lyft')
    access_token = social.extra_data['access_token']
    auth = {'Authorization' : 'Bearer %s' % access_token}

    options = {'headers': auth}

    # http://bravado.readthedocs.io/en/latest/configuration.html#client-configuration
    config = {
        # 'also_return_response': True,
        'validate_responses': False,
        'validate_requests': False,
        'validate_swagger_spec': False,
        'use_models': False
    }

    api = SwaggerClient.from_url(settings.LYFT_YAML, config=config)

    # return options to pass back in during request
    return api, options

class Log():
    
    y = ""
    
    def append(self, x):
        
        self.y = self.y + "\n" + x
        if settings.DEBUG:
            print x
        
    def out(self):
        
        return self.y
        