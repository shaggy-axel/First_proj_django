from django.shortcuts import render

def main_view(request):

    return render(request, 'index.html')

def about_view(request):

    return render(request, 'about_me.html')