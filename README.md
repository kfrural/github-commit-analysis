# Análise de Ritmos de Desenvolvimento Global

Este projeto analisa os padrões de commit em projetos open source populares para entender como desenvolvedores em diferentes fusos horários contribuem durante o dia.

## Instalação

```bash
pip install -r requirements.txt
```

## Uso

1. Obtenha um token pessoal do GitHub
2. Substitua `'SEU_TOKEN_AQUI'` no arquivo `src/github_api.py`
3. Execute:
```bash
python main.py
```

## Resultados

O projeto gera duas visualizações principais:

### Gráfico de Linha Temporal
Mostra a quantidade de commits por hora para cada fuso horário

### Mapa de Calor
Apresenta uma visão geral da distribuição de commits ao longo do dia e entre fusos horários

## Contribuições

Você pode adicionar mais repositórios modificando a lista `repositarios` no arquivo `main.py`.

## Limitações

- O GitHub tem limites de taxa de requisição
- Os dados são coletados apenas dos últimos commits disponíveis
- A detecção do fuso horário é baseada nos timestamps dos commits