from django.shortcuts import render
from .models import Profile,Training,Projects
# Create your views here.
def index(request):
    profile = Profile.objects.all()
    training = Training.objects.all()
    projects = Projects.objects.all()
    return render(request, 'index.html', {'profile':profile, 'training':training, 'projects':projects})