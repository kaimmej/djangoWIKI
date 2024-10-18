from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .forms import EntryForm

from . import util
from markdown2 import Markdown # type: ignore
import os

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

    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            # access the data inside of the form. 
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]

            util.save_entry(name, description)
            return HttpResponseRedirect(reverse("encyclopedia:entry", args=(name,)))

        
        else:
            return render(request, "encyclopedia/create_entry", {
                "form":form
            })
        
    return render(request, "encyclopedia/create_entry.html", {
        "form": EntryForm()
    })

def update_entry(request, wiki_title):    


    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            # access the data inside of the form. 
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]

            util.save_entry(name, description)
            return HttpResponseRedirect(reverse("encyclopedia:entry", args=(name,)))

        
        else:
            description = util.get_entry(wiki_title)
            
            return HttpResponseRedirect(reverse("encyclopedia:update_entry", args=(wiki_title,)), {
                "form":form
            })

    else:
        print("GET")
        # return HttpResponseRedirect(reverse("encyclopedia/update_entry", args=(wiki_title,)), {
        #     "form": EntryForm()
        # })
        return render(request, "encyclopedia/create_entry.html", {
            "form": EntryForm()
        }, args=(wiki_title,))


def search(request):

    print("SEARCH")

    if request.method == 'POST':
        print("POST")
        entry_search = request.POST['q'] 
        print(f"{entry_search=}")
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
                "content": html_content
            })
    else:
        print("GET")
    return
