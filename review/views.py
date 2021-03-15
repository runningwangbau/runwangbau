from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .forms import AnswerForm

from .models import Result
# Create your views here.


def index(request):

    form=AnswerForm(request.POST or None)
    if form.is_valid():
        print("form good")
        obj=Result()
        obj.Name=form.cleaned_data['Name']
        obj.Question=form.cleaned_data['Question']
        obj.save()

        return HttpResponseRedirect('after_test/')
    return render(request,'index.html',{'form':form})

def after_test(request):
    template=loader.get_template("after_test.html")
    result= Result.objects.order_by('-pk')[0]
    context={
        'result':result

    }
    return HttpResponse(template.render(context,request))



