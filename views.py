from django.shortcuts import render
from django.http import JsonResponse
from myapp.forms import AudioForm

def Audio_store(request):
    myvar = False
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            myvar = True
        else:
            myvar = False
        request.session['myvar'] = myvar
    else:
        form = AudioForm()
    return render(request, 'aud.htm', {'form': form})

def getResult(request):
    msg = "Hello World"
    return JsonResponse({'msg': msg})


