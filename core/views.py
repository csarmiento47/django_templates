from django.shortcuts import render, redirect
from .models import Article, Employee
from .forms import ArticleForm, EmployeeForm

# Create your views here.
def root(request):
    return redirect('home')

def home(request):
    context = {'title':'Home | Django Site'}
    return render(request, 'core/index.html', context)

def about(request):
    context = {
        'title':'Quienes somos | Django Site',
        'teams':['Elba Lazo','Aquiles Bailo','Esteban Dido']
    }
    return render(request, 'core/about.html', context)

def contact(request):
    context = {'title':'Contáctanos | Django Site'}
    return render(request, 'core/contact.html', context)

def language(request):
    #lenguajes = ['Python','C++','Java','C#','Javascript','Kotlin','Ruby']
    lenguajes = []
    titulo = 'Lenguajes de Programación'
    
    context = {
        'title':titulo,
        'languages':lenguajes
    }
    
    return render(request, 'core/languages.html', context)
    
def article(request):
    #articulo = request.GET["articulo"]
    #articulos = Article.objects.filter(name__icontains='lala')
    articulos = Article.objects.all()
    context = {
        'articulos' : articulos
    }
    
    return render(request, 'core/article.html',context)

def create_article(request):
    form = ArticleForm()
    
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('article')
    
    context = {
        'form': form,
        'title': 'New Article'
    }
    return render(request,'core/create_article.html',context)
    
    
def employee(request):
    empleados = Employee.objects.all()
    context = {
        'empleados' : empleados,
        'title':'Listado Empleados'
    }
    
    return render(request, 'core/employee.html',context)


def create_employee(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employee')

    context = {
        'form':form,
        'title':'New Employee'
    }
    return render(request, 'core/create_employee.html',context)
