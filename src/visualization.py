import matplotlib.pyplot as plt
import numpy as np

def criar_visualizacao(atividade_por_fuso):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10))
    
    # Gráfico de linha temporal
    fusos = sorted(set(int(k.split('_')[0]) for k in atividade_por_fuso.keys()))
    horas = range(24)
    
    for fuso in fusos:
        valores = [atividade_por_fuso[f"{fuso}_{h}"] for h in horas]
        ax1.plot(horas, valores, label=f'Fuso {fuso}')
    
    ax1.set_xlabel('Hora do Dia')
    ax1.set_ylabel('Número de Commits')
    ax1.set_title('Atividade de Commit por Fuso Horário')
    ax1.legend()
    
    # Mapa de calor
    matriz = np.zeros((len(fusos), 24))
    for i, fuso in enumerate(fusos):
        for hora in range(24):
            matriz[i, hora] = atividade_por_fuso.get(f"{fuso}_{hora}", 0)
    
    im = ax2.imshow(matriz, cmap='hot', aspect='auto')
    ax2.set_xlabel('Hora do Dia')
    ax2.set_ylabel('Fuso Horário')
    ax2.set_title('Mapa de Calor da Atividade de Commit')
    
    plt.colorbar(im, ax=ax2)
    plt.tight_layout()
    return fig