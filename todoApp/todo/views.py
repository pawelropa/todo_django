from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Project

def index(request):
    latest_projects_list = Project.objects.order_by('-pub_date')[:5]
    template = loader.get_template('todo/index.html')
    context = {'latest_projects_list': latest_projects_list}
    return HttpResponse(template.render(context, request))

def detail(request, project_id):
	try:
		project = Project.objects.get(pk=project_id)
	except Project.DoesNotExist:
		raise Http404("Project does not exist")
    return render(request, 'polls/detail.html', {'project': project})

def tasks(request, project_id):
    response = "You're looking at the results of project %s."
    return HttpResponse(response % project_id)