from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User

from dotpy.projects.models import Project

def projects(request, username=None):
    """Page listing all projects (of a user)."""
    projects = Project.objects.order_by('-name')
    if username is not None:
        user = get_object_or_404(User, username=username)
        projects = projects.filter(owner=user)
    projects = projects[:15]
    return render_to_response('projects/projects.html', dict(projects=projects), context_instance=RequestContext(request))

def project(request, pk):
    """Single project page."""
    project = get_object_or_404(Project, pk=pk)
    return render_to_response('projects/project.html', dict(project=project), context_instance=RequestContext(request))
