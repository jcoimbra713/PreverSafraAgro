import pickle
import streamlit as st
import numpy as np

# Carregando a Máquina Preditiva
pickle_in = open('maquina_preditiva_agronegocio.pkl', 'rb') 
maquina_preditiva_agronegocio = pickle.load(pickle_in)

# Essa função é para criação da página web
def main():  
    # Elementos da página web
    # Nesse ponto, você deve personalizar o sistema com sua marca
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:white;text-align:center;">PROJETO PARA PREVER SAFRA</h1> 
    <h2 style ="color:white;text-align:center;">SISTEMA PARA PREVER SAFRA - by João Coimbra </h2> 
    </div> 
    """
      
    # Função do Streamlit que faz o display da página web
    st.markdown(html_temp, unsafe_allow_html=True) 
      
    # As linhas abaixo criam as caixas nas quais o usuário vai inserir os dados da pessoa que deseja prever o diabetes
    ContagemInsetos = st.number_input("Número de Insetos")
    CategoriaCultivo =st.selectbox('Categoria Cultivo', ("Convencional", "Transgênica"))
    TipoSolo = st.selectbox('Tipo Solo', ("Arenoso", "Argiloso "))
    TipoPesticidas = st.selectbox('Tipo Pesticidas', ("Fungicidas", "Herbicidas","Inseticidas"))
    Número_Doses_Semana = st.number_input("Números De Doses Por Semana")
    Número_Semanas_Usadas = st.number_input("Número De Semanas Usadas") 
    NúmeroS_Semanas_Desistência = st.number_input("Número De Semanas De Desistência")
    TemporadaColheita = st.selectbox('Temporada Colheita', ("Inverno", "Primavera","Verão")) 
      
    # Quando o usuário clicar no botão "Verificar", a Máquina Preditiva fará seu trabalho
    if st.button("Verificar"): 
        result, probabilidade = prediction(ContagemInsetos, CategoriaCultivo, TipoSolo, TipoPesticidas, Número_Doses_Semana, Número_Semanas_Usadas, NúmeroS_Semanas_Desistência, TemporadaColheita) 
        st.success(f'Resultado: {result}')
        st.write(f'Probabilidade: {probabilidade}')

# Essa função faz a predição usando os dados inseridos pelo usuário
def prediction(ContagemInsetos, CategoriaCultivo, TipoSolo, TipoPesticidas, Número_Doses_Semana, Número_Semanas_Usadas, NúmeroS_Semanas_Desistência, TemporadaColheita):   
    # Pre-processando a entrada do Usuário    
    if CategoriaCultivo == "Convencional":
        CategoriaCultivo = 0
    else:
        CategoriaCultivo = 1
 
    if TipoSolo == "Arenoso":
        TipoSolo = 0
    else:
        TipoSolo = 1  
    

    if TipoPesticidas == "Fungicidas":
        TipoPesticidas = 0

    if TipoPesticidas == "Herbicidas":
        TipoPesticidas = 1

    else:
        TipoPesticidas = 2

    if TemporadaColheita == "Inverno":
        TemporadaColheita = 0

    if TemporadaColheita == "Primavera":
        TemporadaColheita = 1

    else:
        TemporadaColheita = 2

    # Fazendo a Predição
    parametro = np.array([[ContagemInsetos, CategoriaCultivo, TipoSolo, TipoPesticidas, Número_Doses_Semana, Número_Semanas_Usadas, NúmeroS_Semanas_Desistência, TemporadaColheita]])
    fazendo_previsao = maquina_preditiva_agronegocio.predict(parametro)
    probabilidade = maquina_preditiva_agronegocio.predict_proba(parametro)
   
   
    if (fazendo_previsao == 0).any():
        pred = 'SAUDAVÉL'

    if (fazendo_previsao == 1).any():
        pred = 'DANIFICADA POR PASTICIDADE'

    else:
        pred = 'DANIFICADA POR OUTROS MOTIVOS'

    return pred, probabilidade

if __name__ == '__main__':
    main()