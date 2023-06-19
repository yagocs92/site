from django.urls import path
from .views import Home, Visaogeral, Geral, Pesquisa, Painel, Backlog, Detalhependencia, Vencidos, Atrasados, Mudarstatus, Criarpend, Addcusto
from django.contrib.auth import views as auth_view

app_name = 'gestor'

urlpatterns = [

    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('', Home.as_view(), name='home'),
    path('gestor/', Visaogeral.as_view(), name='visualizarpendencia'),
    path('gestor/geral/', Geral.as_view(), name='geral'),
    path('gestor/geral/pesquisa/', Pesquisa.as_view(), name='pesquisa'),
    path('gestor/painel/', Painel.as_view(), name='painel'),
    path('visualizar/backlogs/recentes', Backlog.as_view(), name='backlog'),
    path('visualizar/backlogs/recentes/<int:pk>', Detalhependencia.as_view(), name='detalhependencia'),
    path('visualizar/backlogs/recentes/<int:pk>/update', Mudarstatus.as_view(), name='mudarstatus'),
    path('visualizar/backlogs/vencidos', Vencidos.as_view(), name='vencidos'),
    path('visualizar/backlogs/antigos', Atrasados.as_view(), name='atrasados'),
    path('visualizar/backlogs/novo', Criarpend.as_view(), name='criarpend'),
    path('visualizar/backlogs/addcusto', Addcusto.as_view(), name='addcusto'),
  
    
]