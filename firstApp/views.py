from django.shortcuts import render
from django.http import HttpResponse

# relative import of forms
from .models import Question
from .forms import QuestionForm

# Create your views here.
def index(request):
  return render(request, 'firstApp/index.html')

def new_question(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form']= form
    return render(request, 'firstApp/new_question.html', context)

