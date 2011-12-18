from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from dotpy.notes.models import Note

def home(request):
    """The notes home page."""
    notes = Note.public_objects.order_by('-votes')[:7]
    return render_to_response('notes/home.html', dict(notes=notes), context_instance=RequestContext(request))

def notes(request):
    """Page listing all notes."""
    notes = Note.pubic_objects.order_by('-created_at')[:15]
    return render_to_response('notes/notes.html', dict(notes=notes), context_instance=RequestContext(request))

def note(request, pk):
    """Single note page."""
    note = get_object_or_404(Note, pk=pk)
    return render_to_response('notes/note.html', dict(note=note), context_instance=RequestContext(request))
