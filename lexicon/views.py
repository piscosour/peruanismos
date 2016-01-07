from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse
from .models import Entry

# Create your views here.

def index(request):
	entry_list = Entry.objects.order_by('entry_name')

	context = {'entry_list': entry_list}

	return render(request, 'lexicon/index.html', context)


def entry_detail(request, entry_id):
	entry = Entry.objects.get(pk=entry_id)

	context = {'entry': entry}

	return render(request, 'lexicon/entry.html', context)