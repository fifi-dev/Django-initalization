from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
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

def questions_lit(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["dataset"] = Question.objects.all()
    
    return render(request, "firstApp/questions.html", context)

# pass id attribute from urls
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["data"] = Question.objects.get(id = id)
    return render(request, "firstApp/detail.html", context)

# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Question, id = id)
 
    # pass the object as instance in form
    form = QuestionForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/firstApp/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "firstApp/update.html", context)