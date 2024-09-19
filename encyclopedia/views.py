from django.http import Http404, HttpResponse
from django.shortcuts import render

from . import util
from markdown2 import Markdown # type: ignore


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, wiki_title):
    
    entry = util.get_entry(wiki_title)
    if entry is None:
        return HttpResponse("Your requested WIKI PAGE was not found.")
    
    markdowner = Markdown()
    markdown_entry = markdowner.convert(entry)  


    entry_content = util.get_entry(wiki_title)
    
    return render(request, "encyclopedia/entry.html", {
        "entry_title": wiki_title,
        "entry_content": markdown_entry
    })

def create_entry(request):    
    return render(request, "encyclopedia/create_entry.html")