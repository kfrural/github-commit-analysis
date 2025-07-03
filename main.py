from src.github_api import obterCommits
from src.data_processor import agrupar_por_fuso
from src.visualization import criar_visualizacao

async def main():
    repositarios = [
        'facebook/react',
        'vuejs/vue',
        'tensorflow/tensorflow',
        'torvalds/linux'
    ]
    
    todos_commits = []
    for repo in repositarios:
        commits = await obterCommits(repo)
        todos_commits.extend(commits)
    
    atividade_por_fuso = agrupar_por_fuso(todos_commits)
    fig = criar_visualizacao(atividade_por_fuso)
    fig.savefig('analise_commits.png')

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())