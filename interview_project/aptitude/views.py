from django.shortcuts import render
import requests

response = requests.get('https://aptitude-api.vercel.app/Random')
question_data = response.json()
question = question_data["question"]

def index(request):
    return render(request, 'aptitude/index.html', {
        'question' : question,
    })