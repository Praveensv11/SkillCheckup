from django.shortcuts import render
import requests

results = []
for i in range(3):
    response = requests.get('https://aptitude-api.vercel.app/Random')
    results.append(response.json())

def index(request):
    return render(request, 'aptitude/index.html', {
        'results' : results,
    })