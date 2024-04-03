from django.shortcuts import render
from django.http import JsonResponse
from myapp.forms import AudioForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


transcript_text = ''

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

def generateActionItems():
    return None

def generateSummary(text):
    items = generateActionItems()
    return "ok working fine"
@csrf_exempt
def getScript(request):
    global transcript_text
    
    if request.method == 'POST':
        data = json.loads(request.body)
        transcript_text = data.get('transcript', '')
        if transcript_text:
            result = generateSummary(transcript_text)
            return JsonResponse({"result":result})
        return JsonResponse({'status': 'Transcript is empty pls check it once'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt  
def show_transcript(request):
    global transcript_text
    return JsonResponse({'transcript': transcript_text})

