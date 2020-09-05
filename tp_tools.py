"""This file contain the style applied to markdown in the notebook !!
"""
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly import tools
import plotly.graph_objs as go
import numpy as np
from exp import cumulative_regret, logarithmic_indices



def change_font():
    """Une méthode qui retourme le fichier HTML et CSS adéquat pour les fonts dans jupyter.
    """

    html = """
    <style>
    
    .rendered_html {
         font-size: 22px; 
         font-family: Garamond;
         line-height: 140%;
         text-align: justify;
         text-justify: inter-word;
    }

    div.text_cell_render h1 { /* Main titles bigger, centered */
        text-align:center;
    # }
    
    </style>"""

    return html

    def plot_cumulative_regret(logs, labels, n_games=10, n_iter=1000):
        """Représentation du regret cumulé des algorithmes données en input.
    
        Arguments:
            logs {list} -- Liste des logs des algorithmes de 
            labels {list} -- Liste des labels pour la représentation graphique.
        
        Keyword Arguments:
            n_games {int} -- Nombre de jeux effectué par chaque algorithme (default: {10})
            n_iter {int}  -- Nombre d'essais par jeu (default: {1000})
        
        Returns:
            plot -- plotly object for graph
        """
    
        inds = logarithmic_indices(n_iter, 100)

        fig = tools.make_subplots(rows=1, cols=1)
        for i in range(len(logs)):
            plot = go.Scatter(x=inds + 1, y=cumulative_regret(logs[i])[inds], mode = 'lines', name = labels[i])
            fig.append_trace(plot, 1, 1)

        fig['layout'].update(height=600, width=1000, title="Evolution du Regret cumulé selon le nombre d'itérations")
        

        # title="Evolution du Regret cumulé selon le nombre d'itérations",
        #     xaxis=go.layout.XAxis(title="Nombre d'essais"),
        #     yaxis=go.layout.YAxis(title='Regret Cumulé')

        # go.Layout(

        # )

        # n_games = 10 #Doubler du nombre de jeux par rapport à la dernière fois
        # n_iter  = 300 # Augmenter le nombre d'itérations de 1000 encore.
        # inds = logarithmic_indices(n_iter, 100) #Afficher seulement 100 points au toytal
        # c_range = range(10,13)

        # n_rows = 2
        # n_cols = 2
        # fig = tools.make_subplots(rows=n_rows, cols=n_cols)

        # for row in range(1,n_rows+1):
        #     for col in range(1,n_cols+1):
        #         for c in c_range:
        #             log = games(EpsilonNGreedy(nb_arms=len(environment), c=c), environment, n_iter, n_games)
        #             plot = go.Scatter(x=inds + 1, y=cumulative_regret(log)[inds], mode = 'lines', name = 'EG, c = %d'%c)
        #             fig.append_trace(plot, row,col)
        # fig['layout'].update(height=600, width=900, title="Evolution du Regret cumulé")
        # iplot(fig)
        #logs_EG = []
        #labels  = []
        #for c in c_range:
        #    logs_EG.append(games(EpsilonNGreedy(nb_arms=len(environment), c=c), environment, n_iter, n_games))
        #    labels.append('EG, c = %d'%c)
        #plot_cumulative_regret(logs=logs_EG, labels=labels, n_iter=n_iter, sub_plots=(3,2))
        return iplot(fig)
