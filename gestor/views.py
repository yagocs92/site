from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Equipamentos_maq, Pendencias, Custo
from django.urls import reverse


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('gestor:geral')        
        else:
            return super().get( request, *args, **kwargs)

class Visaogeral(LoginRequiredMixin, TemplateView):
    template_name = "visualizapendencias.html"

class Geral(LoginRequiredMixin, ListView):
    template_name = 'geral.html'
    model = Equipamentos_maq

class Pesquisa(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Equipamentos_maq
    
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('q')
        if termo_pesquisa:
            object_list = self.model.objects.filter(tag__icontains= termo_pesquisa)
            return object_list
        else:
            return None

class Painel(LoginRequiredMixin, TemplateView):
    template_name = 'painel.html'

class Backlog(LoginRequiredMixin, ListView):
    template_name = 'recentes.html'
    model = Pendencias

class Detalhependencia(LoginRequiredMixin, DetailView):
    template_name = "detalhespendencias.html"
    model = Pendencias
    
    def get_context_data(self, **kwargs):
        context = super(Detalhependencia, self).get_context_data(**kwargs)
        pendencias_relacionadas = Pendencias.objects.filter(list_maquina=self.get_object().list_maquina)
        context['pendencias_relacionadas'] = pendencias_relacionadas
        return context

class Mudarstatus (LoginRequiredMixin, UpdateView):
    template_name = 'mudstatus.html'
    model = Pendencias
    fields = ['status']
    
    def get_success_url(self):
        return reverse('gestor:backlog')
    
     
class Atrasados(LoginRequiredMixin, ListView):
    template_name = 'atrasados.html'
    model = Pendencias

class Vencidos(LoginRequiredMixin, ListView):
    template_name = 'vencidos.html'
    model = Pendencias

class Criarpend (LoginRequiredMixin, CreateView):
    template_name = "criarpend.html"
    model = Pendencias
    fields = ['maquina', 'list_maquina', 'categoria', 'titulo', 'corpo', 'data_criacao', 'tempo_hora_homem', 'status', 'thumb' ]
    
    def get_success_url(self):
        return reverse('gestor:backlog')

class Addcusto (LoginRequiredMixin, CreateView):
    template_name = "addcusto.html"
    model = Custo
    fields = ['backlog', 'codigo', 'ni', 'item', 'qtd', 'preco_unit' ]
    
    def get_success_url(self):
        return reverse('gestor:geral')


   