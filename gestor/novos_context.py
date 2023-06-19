from .models import Pendencias, Custo, Equipamentos_maq

def lista_pendencias_recentes(request):
    lista_penndencia = Pendencias.objects.all().order_by('-data_criacao')[0:10]
    return {"lista_pendencias_recentes":lista_penndencia}

def lista_pendencias_antigas(request):
    lista_antigas = Pendencias.objects.all().order_by('data_criacao')[0:10]
    return {"lista_pendencias_antigas":lista_antigas}

def lista_pendencias_vencidas(request):
    lista_vencidas = Pendencias.objects.filter(status='vencido') 
    return {"lista_pendencias_vencidas":lista_vencidas}

def lista_desembolso(request): 
    custo = Custo.objects.raw( 
        ''' 
        SELECT 1 as id, gestor_custo.backlog_id as pend, sum(gestor_custo.qtd * gestor_custo.preco_unit) as mult \
        FROM gestor_custo, gestor_pendencias \
        WHERE gestor_custo.backlog_id = gestor_pendencias.id \
        GROUP by gestor_custo.backlog_id
    ''')

    return {'lista_desembolso' : custo}

def lista_pendmaq(request): 
    dist = Equipamentos_maq.objects.raw( 
        ''' 
        SELECT 1 as id, gestor_equipamentos_maq.id, gestor_equipamentos_maq.tag, gestor_equipamentos_maq.padrinho, count(gestor_pendencias.id)  as qtd \
        FROM gestor_equipamentos_maq, gestor_pendencias \
        WHERE gestor_equipamentos_maq.id = gestor_pendencias.maquina_id \
        GROUP BY gestor_equipamentos_maq.id
    ''')

    return {'lista_pendmaq' : dist}
