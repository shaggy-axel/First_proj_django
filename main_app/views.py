from django.shortcuts import render

def main_view(request):
	
	skills_list = [ 
		'Python 3',
		'Linux', 'DataBase', 
		'Web- django, html, css, js',
		'english B1, czech B2, russian Native',
		'Git, flask, celery, redis',
		'mongodb, column databases, design patterns'
		]
	
	return render(request, 'index.html', {'skills':skills_list})

def portfolio_view(request):

	ids_list = [

		'id-1','id-2','id-3','id-4','id-5','id-6',
		'id-7','id-8','id-9','id-10','id-11','id-12','id-13',
		'id-14','id-15','id-16','id-17','id-18','id-19','id-20',
		]

	return render(request, 'portfolio.html',{'ids':ids_list})