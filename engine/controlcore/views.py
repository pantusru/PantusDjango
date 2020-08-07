import os
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
import urllib.request, json
from django.contrib import messages
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as BS


# Create your views here.



