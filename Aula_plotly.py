import dash
from dash import dcc,html
from dash.dependencies import Input, Output

import plotly.graph_objects as go
# DADOS
dados_conceito=dict(
    java={'variáveis':3,'condicionais':6,'loops':2,'poo':1,'funções':1},
    python={'variáveis':9,'condicionais':8,'loops':5,'poo':7,'funções':4},
    sql={'variáveis':4,'condicionais':2,'loops':5,'poo':4,'funções':6},
    golang={'variáveis':6,'condicionais':8,'loops':9,'poo':8,'funções':3},
    javascript={'variáveis':8,'condicionais':5,'loops':2,'poo':9,'funções':4}

)
color_map=dict(
    java='red',
    python='blue',
    sql='lightblue',
    golang='orange',
    javascript='yellow'
)

app=dash.Dash(__name__)


# __________________________LAYOUT__________________________________

app.layout=html.Div([
    html.H1('Ana Carolina',style={'textAlign':'center'}
            ),
    html.Div(
        dcc.Dropdown(
            id='dropdown_linguagens',
            options=[
                {'label': 'Java', 'value':'java'},
                {'label': 'Python', 'value':'python'},
                {'label': 'SQL', 'value':'sql'},
                {'label': 'Golang', 'value':'golang'},
                {'label': 'JavaScript', 'value':'javascript'}
            ],
            value=['java'],
            multi=True,
            style={'width':'70%','margin':'0 auto'}
         )
    ),
    dcc.Graph(
        id='scatter_plot'
    )
])
# _________________________CALLBACKS________________________________

@app.callback(
    Output('scatter_plot', 'figure'),
    [Input('dropdown_linguagens','value')]
)
def atualizar_scatter(linguagens_selecionadas):
    
    scatter_trace = []

    for linguagens in linguagens_selecionadas:
        dados_linguagens=dados_conceito[linguagens]
        for conceito, conhecimento in dados_linguagens.items():
            scatter_trace.append(
                go.Scatter(
                    x=[conceito],
                    y=[conhecimento],
                    mode='markers',
                    name=linguagens.upper(),
                    marker=dict(
                        size=50, color=color_map[linguagens]),
                    showlegend=False
                )
            )

    scatter_layout= go.Layout(
        title='Minhas Linguagens',
        xaxis=dict(title='Conceitos',showgrid=False),
        yaxis=dict(title='Nível de Conhecimento',showgrid=False)
    )

    return{'data': scatter_trace}

if __name__== '__main__':

    app.run_server(debug=True)