from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User

import logging

from dotpy.notes.models import Note

logger = logging.getLogger(__name__)

def notes(request, username=None):
    """Page listing all notes (of a user)."""
    logger.debug('Accessing notes... username: %s', username)
    notes = Note.public_objects.order_by('-created_at')
    if username is not None:
        user = get_object_or_404(User, username=username)
        notes = notes.filter(owner=user)
    notes = notes[:15]
    return render_to_response('notes/notes.html', dict(notes=notes), context_instance=RequestContext(request))

def note(request, pk):
    """Single note page."""
    note = get_object_or_404(Note, pk=pk)
    return render_to_response('notes/note.html', dict(note=note), context_instance=RequestContext(request))
