from django.shortcuts import render, redirect
# from django.http import HttpResponse;
from .models import Activity;
from .forms import ActivityForm
from .serializers import ActivitySerializer

from rest_framework import generics


# Create your views here.

def index(request):
    spec_list = Activity.objects.all();
    context = {'spec_list' : spec_list};
    return render(request, 'spec/spec_main.html', context);


def create_spec(request):
    if request.method == "POST":
        form = ActivityForm(request.POST);
        if form.is_valid():
            spec = form.save();
            spec.save();
            return redirect('spec:index');
    else:
        form = ActivityForm();
    context = {'form' : form};
    return render(request, 'spec/spec_create.html', context);



class ActivityListCreateAPIViews(generics.ListCreateAPIView):
    queryset = Activity.objects.all();
    serializer_class = ActivitySerializer;







