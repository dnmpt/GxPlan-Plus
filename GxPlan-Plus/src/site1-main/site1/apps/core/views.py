from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.template.defaulttags import register

from .forms import FormUser1,ProjectForm, TaskForm
from django.contrib.auth.decorators import login_required         #Login
from django.contrib.auth.views import LogoutView                  #Logout
from datetime import datetime
from .models import Category,Project,Task, Note,Message,Authorization

dict_status = {0:'Canceled',1:'Scheduled',2:'In Progress',3:'Done'}

# FILTERS for TEMPLATES
@register.filter
def date_only(my_date):
    return my_date.strftime("%d/%m/%Y")

@register.filter
def date_calendar(my_date):
    return my_date.strftime("%Y-%m-%d")

@register.filter
def dict_value(my_dict, key):
    return my_dict[key]

@register.filter
def classify(value):
    prio = {0:'Lower',1:'Low',2:'Medium',3:'High',4:'Higher'}
    if value > 19:
        return prio[4] # 19 and 20 are higher ...
    else :
        return prio[int(value/5)]

# Create your views here.

def index(request):

    categs = Category.objects.order_by('name')
    data = {'categs':categs}
    return render(request,'index.html', data)


def ProjectsList(request, ctg_id):
    categs = Category.objects.order_by('name')
    ctg = Category.objects.get(pk=ctg_id)

    # Get the variable (list_status) by GET to filter view of Projects
    view_status = request.GET.get('list_status')
    if not view_status:
        projs = Project.objects.filter(categ = ctg).order_by('name')
    else:
        projs = Project.objects.filter(categ = ctg, status=view_status).order_by('name')

    data = {'project_list':projs,'categs':categs,'ctg':ctg,'status':dict_status}
    return render(request,'category.html', data)


# EDIT PROJECT by GET
def editProj(request, id):
    categs = Category.objects.order_by('name')
    proj = Project.objects.get(id=id)
    ctg = Category.objects.get(pk=proj.categ.id)
    template = loader.get_template('editproj.html')
    data = {
        'proj': proj,
        'categs' : categs,
        'ctg' : ctg,
        'status': dict_status,
        }
    return HttpResponse(template.render(data, request))


# EDIT PROJECT by POST
def editProjRecord(request, id):
    # Get values by POST
    if request.method == 'POST': # Safeguard ...
        ctg_ = request.POST['ctg_']
        ctg = Category.objects.get(pk=ctg_)
        
        name = request.POST['name']
        notes = request.POST['notes']
        start_date_str = request.POST['start_date']
        end_date_str = request.POST['end_date']
        status_ = request.POST['status_']

        proj = Project.objects.get(id=id)
        try:  
            image = request.FILES['image'] # Request Files for image upload ...
            proj.image = image
        except:
            proj.image=proj.image
        #Update record
        proj.categ = ctg
        proj.name = name
        proj.notes = notes
        if start_date_str:
            proj.start_date = datetime.strptime(start_date_str,"%Y-%m-%d")
        if end_date_str:
            proj.end_date = datetime.strptime(end_date_str,"%Y-%m-%d")
        proj.status = status_
        proj.save() # Adicionar um Try/Except ...

        #Get data to render previous template
        return redirect('projects_list', ctg.id)
    else: # If somehow is GET ... Not will Happen , right ???
        return HttpResponseRedirect(reverse('index')) # Return to 'index' but can't pass arguments ...


def newProject(request, ctg_id):
    msg =''
    categs = Category.objects.order_by('name')
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        # Data from request.POST
        ctg_ = request.POST['ctg_']
        ctg = Category.objects.get(pk=ctg_)
        if form.is_valid():     
            proj = Project()
            proj.categ = ctg
            # Data from FORM data
            proj.name = form.cleaned_data['_name']
            proj.notes = form.cleaned_data['_notes']
            proj.start_date = form.cleaned_data['_start_date']
            proj.end_date = form.cleaned_data['_end_date']
            proj.status = form.cleaned_data['_status']

            # Data from request.POST
            try:  
                image = request.FILES['image'] # Request Files for image upload ...
                proj.image = image
            except:
                proj.image="media/new_project.png" # Image by default ...
        
            proj.save() # Adicionar um Try/Except ...
            return redirect("projects_list", ctg.id) # redirects do url 'projects_list' with argument 'ctg_id'
        else:
            msg = form.errors
            data = {'form':form,'msg':msg,'categs':categs,'ctg':ctg}  
            return render(request,"new_project.html", data)
    else:
        form = ProjectForm()
        ctg = Category.objects.get(pk=ctg_id)
        data = {'form':form,'msg':msg,'categs':categs,'ctg':ctg}    
        return render(request,"new_project.html", data)


def TaskList(request, proj_id):
    categs = Category.objects.order_by('name')
    proj = Project.objects.get(pk=proj_id)
    ctg = Category.objects.get(pk=proj.categ.id)
    tasks = Task.objects.filter(project = proj).order_by('-priority')
    notes = Note.objects.filter(task__in=tasks).order_by('-revision_date')
    authors = Authorization.objects.filter(task__in=tasks).order_by('user_authorized')
    data = {'task_list':tasks,'notes':notes,'authors':authors,'categs':categs,'ctg':ctg,'proj':proj,'status':dict_status}
    return render(request,'project.html', data)

# EDIT task (uses same FORM as create New, but FORM has a initial dictionary)
def editTask(request, task_id):
    msg =''
    categs = Category.objects.order_by('name')
    task = Task.objects.get(pk=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        # Data from request.POST
        if form.is_valid():
            task.name = form.cleaned_data['_name']
            task.value = form.cleaned_data['_value'] 
            task.urgency = form.cleaned_data['_urgency'] 
            task.compliance = form.cleaned_data['_compliance']
            task.effort = form.cleaned_data['_effort'] 
            task.priority = (int(task.effort)  + 2 * int(task.urgency) + 3 * int(task.compliance))/1.5 + int(task.value) - 5
            task.cost = form.cleaned_data['_cost']
            task.progress = form.cleaned_data['_progress']
            task.start_date = form.cleaned_data['_start_date']
            task.end_date = form.cleaned_data['_end_date']
            task.status = form.cleaned_data['_status']

            task.save() # Adicionar um Try/Except ...
            return redirect("task_list", task.project.id)
        else:
            msg = form.errors
            data = {'form':form,'msg':msg,'categs':categs,'task':task}  
            return render(request,"edittask.html", data)
    else:
        # Create initial dictionary for data to existing FORM
        initial_data = {
            "_name" : task.name,
            "_value" : task.value,
            "_urgency" : task.urgency,
            "_compliance" : task.compliance,
            "_effort" : task.effort,
            "_cost" : task.cost,
            "_start_date" : task.start_date,
            "_end_date" : task.end_date,
            "_progress" : task.progress,
            "_status" : task.status
            }
        form = TaskForm(request.POST or None,initial=initial_data)  # Form with initial_data
        data = {'form':form,'msg':msg,'categs':categs,'task':task}       
        return render(request,"edittask.html", data)

# Create New Task
def newTask(request, proj_id):
    msg =''
    categs = Category.objects.order_by('name')
    proj = Project.objects.get(pk=proj_id)
    ctg = Category.objects.get(pk=proj.categ.id) # Need this to check user accessability
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        # Data from request.POST
        if form.is_valid():
            task = Task()
            task.project = proj
            task.name = form.cleaned_data['_name']
            task.value = form.cleaned_data['_value'] 
            task.urgency = form.cleaned_data['_urgency'] 
            task.compliance = form.cleaned_data['_compliance']
            task.effort = form.cleaned_data['_effort'] 
            task.priority = (int(task.effort)  + 2 * int(task.urgency) + 3 * int(task.compliance))/1.5 + int(task.value) - 5
            task.cost = form.cleaned_data['_cost']
            task.progress = form.cleaned_data['_progress']
            task.start_date = form.cleaned_data['_start_date']
            task.end_date = form.cleaned_data['_end_date']
            task.status = form.cleaned_data['_status']

            task.save() # Adicionar um Try/Except ...
            return redirect("task_list", proj.id)
        else:
            msg = form.errors
            data = {'form':form,'msg':msg,'categs':categs,'proj':proj,'ctg':ctg}  
            return render(request,"new_task.html", data)
    else:
        form = TaskForm()
        data = {'form':form,'msg':msg,'categs':categs,'proj':proj,'ctg':ctg}    
        return render(request,"new_task.html", data)

# Model Form por POST. 
# Aceder por : http://127.0.0.1:8000/news24x7/registo/
def registerUser(r):
    msg =''
    if r.method == 'POST': # Verifica se o método é POST. Isso significa que o user carregou no botão (não acedeu pelo endereço) !
        form = FormUser1(r.POST) # A classe apanha o dicionário enviado pelo formulário por POST
        if form.is_valid():
            form.save()
            return redirect("index") # redireciona para a página 'index'
        else:
            msg = form.errors
    return render(r,"registration/register.html", {'form':FormUser1(),'msg':msg}) # Cria o objecto da classe 'FormUser1' e passa 'msg'
