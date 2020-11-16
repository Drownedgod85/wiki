from django.http import Http
from django.shortcuts import render
from django import forms
import markdown2
import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    markdowner = Markdown()
    entryPage = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control col-md-8 col-lg-8;'}))
    if entryPage is None:
        return render(request, "enclyclopedia/nonExistingEntry.html", {
            "entryTitle": entry
        })
    else:
        return render(request,render(request, "encyclopedia/entry.html", {
            "entry": markdowner.convert(entryPage),
            "entryTitle": entry
            })
