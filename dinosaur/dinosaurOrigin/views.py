from django.shortcuts import render



def dinosaurOrigin(request):
    '''
    Render the main page
    '''
    context = {}
    return render(request, 'dinosaurOrigin/dinosaurOrigin.html', context)