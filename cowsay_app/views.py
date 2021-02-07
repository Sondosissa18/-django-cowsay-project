from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect, reverse
from cowsay_app.models import Cowtext
import subprocess
from .forms import NameForm
from cowsay import *

def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            
            data = form.cleaned_data
            Cowtext.objects.create(
                    text=data["text"],
            )
            result = subprocess.check_output(["cowsay", data["text"]])
            textpre = result.decode('UTF-8')
            form = NameForm()
            print(result)
            
            
            return render(request, "index.html", {'form': form , 'result': textpre})

    else:
        form = NameForm()


    return render(request, "index.html", {'form': form})


def cow_history(request):
    # my_history = Cowtext.objects.all()
    my_history = Cowtext.objects.all().order_by('-id')[:10]
    return render(request, "history.html", {"history": my_history})