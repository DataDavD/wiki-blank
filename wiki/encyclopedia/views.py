from django.http.response import Http404, HttpResponse
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    html_response = util.convert_to_html(title)
    if html_response is None:
        raise Http404("Entry does not exist")
    
    return HttpResponse(html_response)
