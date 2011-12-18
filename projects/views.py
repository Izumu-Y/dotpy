from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from dotpy.projects.models import Project

def projects(request):
    """Page listing all projects."""
    projects = Project.objects.order_by('-name')[:15]
    return render_to_response('projects/projects.html', dict(projects=projects), context_instance=RequestContext(request))

def project(request, pk):
    """Single project page."""
    project = get_object_or_404(Project, pk=pk)
    return render_to_response('projects/project.html', dict(project=project), context_instance=RequestContext(request))
