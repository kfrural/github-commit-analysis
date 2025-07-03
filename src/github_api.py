import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN_GITHUB')

async def obterCommits(repositorio, pagina=1):
    owner, repo = repositorio.split('/')
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    params = {
        'per_page': 100,
        'page': pagina
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()