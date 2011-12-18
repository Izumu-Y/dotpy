from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User

from dotpy.notes.models import Note
from dotpy.projects.models import Project

def home(request):
    """The home page."""
    hot_notes = Note.public_objects.order_by('-votes')[:7]
    hot_projects = Project.objects.order_by('-votes')[:7]
    return render_to_response('home.html',
            dict(hot_notes=hot_notes, hot_projects=hot_projects),
            context_instance=RequestContext(request))

def users(request):
    """Page listing all users."""
    users = User.objects.filter(is_active=True).order_by('username')[:15]
    return render_to_response('users.html', dict(users=users), context_instance=RequestContext(request))

def user(request, username):
    """The user page."""
    user = get_object_or_404(User, username=username)
    return render_to_response('user.html', dict(user=user), context_instance=RequestContext(request))
