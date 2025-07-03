from datetime import datetime
import pytz

def extrair_fuso_horario(commit):
    timestamp = commit['commit']['author']['date']
    dt = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
    dt_utc = pytz.UTC.localize(dt)
    fuso_horario = dt_utc.tzinfo.utcoffset(dt_utc).total_seconds() / 3600
    return round(fuso_horario)

def agrupar_por_fuso(commits):
    atividade_por_fuso = {}
    for commit in commits:
        fuso = extrair_fuso_horario(commit)
        hora = datetime.strptime(
            commit['commit']['author']['date'], 
            '%Y-%m-%dT%H:%M:%SZ'
        ).hour
        
        chave = f"{fuso}_{hora}"
        atividade_por_fuso[chave] = atividade_por_fuso.get(chave, 0) + 1
    return atividade_por_fuso