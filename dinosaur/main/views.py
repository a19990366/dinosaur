from django.shortcuts import render
import datetime


def main(request):
    '''
    Render the main page
    '''
    now = datetime.datetime.now()
    context = {"now":now}
    return render(request, 'main/main.html', context)