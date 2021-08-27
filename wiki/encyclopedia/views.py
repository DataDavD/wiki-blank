from django.http.response import Http404
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    content = util.get_entry(entry)
    if content is None:
        raise Http404("Entry does not exist")
    
    return render(request, "encyclopedia/entry_page.html", {
        "content" : content
        ## convert  md
    })