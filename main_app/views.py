from django.shortcuts import render

class Person():
    def __init__(self, name):
        self.name = name

def main_view(request):
    p1 = Person('Kate')
    name = 'Diana'
    return render(request, 'index.html', {'name': name, 'person':p1})

def about_view(request):

    return render(request, 'about_me.html')