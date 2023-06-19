from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

LISTA_CATEGORIA = (
    ("maquina base", "Maquina Base"),
    ("cabecote", "Cabeça Processadora"),
)

LISTA_SIM_NAO = (
    ('sim', 'Sim'),
    ('nao', 'Não'),
)
LISTA_STATUS = (
    ('no prazo', 'No prazo'),
    ('vencido', 'Vencido'),
    ('concluido', 'Concluido'),
)

LISTA_MAQUINAS = (
    ('F-HVE-0339', 'F-HVE-0339'),
    ('F-HVE-0341', 'F-HVE-0341'),
    ('F-HVE-0343', 'F-HVE-0343'),
    ('F-HVE-0347', 'F-HVE-0347'),
    ('F-HVE-0539', 'F-HVE-0539'),
    ('F-HVE-0540', 'F-HVE-0540'),
    ('F-HVE-0541', 'F-HVE-0541'),
    ('F-HVE-0542', 'F-HVE-0542'),
    ('F-HVE-0543', 'F-HVE-0543'),
    ('F-HVE-0544', 'F-HVE-0544'),
)

LISTA_LETRAS = (
    ('Letra A', 'Letra A'),
    ('Letra B', 'Letra B'),
    ('Letra C', 'Letra C'),
    ('Letra D', 'Letra D'),
)

class Instancia (models.Model):
    modulo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)

    def __str__(self):
        return self.modulo

class Equipamentos_maq (models.Model):
    tag = models.CharField(max_length=50)
    horas_motor = models.CharField('Horimetro:', max_length=50)
    imagem_maquina = models.ImageField(upload_to='thumb_maquinas')
    modulo = models.ForeignKey("Instancia", related_name='maquinas', on_delete=models.CASCADE )
    padrinho = models.CharField(max_length=80, choices=LISTA_LETRAS, default='Letra A')
    
    def __str__(self):
        return self.tag

class Pendencias (models.Model):

    maquina = models.ForeignKey("Equipamentos_maq", related_name='pendencias', on_delete=models.CASCADE)
    list_maquina = models.CharField('Repita a Maquina Selecionada:', max_length=50, choices=LISTA_MAQUINAS, default='Selecione')
    categoria = models.CharField(max_length=50, choices=LISTA_CATEGORIA)
    titulo = models.CharField(max_length=50)
    corpo = models.TextField(max_length=1000)
    data_criacao = models.DateTimeField('Data de Criação',default=timezone.now)
    tempo_hora_homem = models.FloatField('Tempo Estimado de Manutenção (HH)',max_length=100, default=1.0)
    status = models.CharField(max_length=100, choices=LISTA_STATUS)
    thumb = models.ImageField('Foto da Pendencia:', upload_to='thumb_pendencias', default='default.jpg')

    def __int__(self):
        return self.pk


class Custo (models.Model):
    backlog = models.ForeignKey("Pendencias", on_delete=models.CASCADE, related_name='materiais', null=True, default=1)
    codigo = models.CharField(max_length=100)
    ni = models.CharField(max_length=100)
    item = models.CharField(max_length=100)  
    qtd = models.IntegerField(max_length=100)
    preco_unit = models.FloatField(max_length=100)
    
    def __str__(self):
        return  self.item