from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from forms_builder.forms.models import Form

def index(request):
    forms =  Form.objects.all()
    return render_to_response('index.html', {'forms': forms}, context_instance=RequestContext(request))
