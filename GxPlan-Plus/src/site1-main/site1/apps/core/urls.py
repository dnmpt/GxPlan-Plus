from django.urls import path
from . import views

# registar os urls
# path(caminho,view,nome)
urlpatterns = [
    path('', views.index,name='index'),
    path('register/', views.registerUser, name = "register"),
    path('logout/', views.LogoutView.as_view(next_page='/'), name = "logout"),
    path('category/<int:ctg_id>', views.ProjectsList,name='projects_list'),
    path('project/<int:proj_id>', views.TaskList,name='task_list'),
    path('project/edit/<int:id>', views.editProj, name='edit_proj'),
    path('project/edit/editrecord/<int:id>', views.editProjRecord, name='edit_projrecord'),
    path('category/new/<int:ctg_id>', views.newProject,name='new_project'),
    path('project/new/<int:proj_id>', views.newTask,name='new_task'),
    path('task/edit/<int:task_id>', views.editTask,name='edit_task'),
]
