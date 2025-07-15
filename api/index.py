from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse(content={"message": "API está online!"})



dados_missas_dic = {
    1: {'Paróquia': 'CATEDRAL - PARÓQUIA SAGRADO CORAÇÃO DE JESUS', 'Arquidiocese': 'Londrina', 'Decanato': 'Centro', 'Cidade': 'Londrina', 'Dia': 'Segunda', 'Horário': '07h00', 'Observação': nan},
    2: {'Paróquia': 'CATEDRAL - PARÓQUIA SAGRADO CORAÇÃO DE JESUS', 'Arquidiocese': 'Londrina', 'Decanato': 'Centro', 'Cidade': 'Londrina', 'Dia': 'Segunda', 'Horário': '12h00', 'Observação': nan},
    3: {'Paróquia': 'CATEDRAL - PARÓQUIA SAGRADO CORAÇÃO DE JESUS', 'Arquidiocese': 'Londrina', 'Decanato': 'Centro', 'Cidade': 'Londrina', 'Dia': 'Terça', 'Horário': '07h00', 'Observação': nan},
    4: {'Paróquia': 'CATEDRAL - PARÓQUIA SAGRADO CORAÇÃO DE JESUS', 'Arquidiocese': 'Londrina', 'Decanato': 'Centro', 'Cidade': 'Londrina', 'Dia': 'Terça', 'Horário': '12h00', 'Observação': nan},
    5: {'Paróquia': 'CATEDRAL - PARÓQUIA SAGRADO CORAÇÃO DE JESUS', 'Arquidiocese': 'Londrina', 'Decanato': 'Centro', 'Cidade': 'Londrina', 'Dia': 'Quarta', 'Horário': '07h00', 'Observação': nan},
}


# Rota dinâmica (GET)
@app.get("/paroquias")
def lista_paroquias(dados_missas_dic):
    return dados_missas_dic








# ####
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import pandas as pd
# import numpy as np
# from mangum import Mangum


# app = FastAPI()


# Configurar CORS
#app.add_middleware(
#    CORSMiddleware,
#    allow_origins=["*"],  # Permitir todas as origens
#    allow_credentials=True,
#    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc.)
#    allow_headers=["*"],  # Permitir todos os cabeçalhos
#)



    
# def load_data(url):
#     df = pd.read_csv(url)
#     return df

# df = load_data('https://raw.githubusercontent.com/santahora/santahora/main/horarios_missas_id_2.csv')

# # Rota de teste (GET)
# @app.get("/")
# def read_root():
#     return {"mensagem": "API is up!"}

# # Rota dinâmica (GET)
# @app.get("/missas/paroquia/{nome_paroquia}")
# def missas_paroquia(nome_paroquia: str):
#     df_cut = df[df['Paróquia'] == nome_paroquia]
#     df_cut = df_cut.replace({np.nan: None})

#     return df_cut.set_index('ID missa').to_dict(orient='index')


# # Rota dinâmica (GET)
# @app.get("/paroquias")
# def lista_paroquias():
#     dic_lista_paroquias = {'lista_paroquias': list(df['Paróquia'].unique())}
#     return dic_lista_paroquias

# # Adaptador Mangum para Vercel Serverless Functions
# # handler = Mangum(app)
