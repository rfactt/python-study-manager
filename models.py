STATUS_VALIDOS = ["pendente", "fazendo", "concluido"]
PRIORIDADES_VALIDAS = ["baixa", "media", "alta"]

def status_valido(status):
    return status in STATUS_VALIDOS

def prioridade_valida(prioridade):
    return prioridade in PRIORIDADES_VALIDAS