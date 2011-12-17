from django.shortcuts import render_to_response
from django.template import RequestContext

from notes.models import Note

def home(request):
    """The home page."""
    hot_notes = Note.public_objects.order_by('-votes')[:7]
    return render_to_response('home.html', dict(hot_notes=hot_notes), context_instance=RequestContext(request))
