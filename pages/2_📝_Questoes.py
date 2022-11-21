import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import streamlit as st
import numpy as np
import plotly.express as px 

import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

import Home


# ======================================================================================        
# Questao 1 - quais são os imóveis que a House Rocket deveria comprar e por qual preço ?

def filter_recomendation (data1):
# ---filtro compra ou nao compra

    options = ['Recomendado', 'Nao recomendado', 'Todos'] 
    f_recomendation = st.selectbox('Filtro de recomendacao', options=options)

    if (f_recomendation == 'Recomendado'):
        data_selected = data1.loc[data1['buy_recomendation']=='buy',:]

    elif (f_recomendation == 'Nao recomendado'):
        data_selected = data1.loc[data1['buy_recomendation']=='not_buy',:]

    else:
        data_selected = data1.copy()
    
    return data_selected
    
    

def map_buy_recomendation(data_selected):
#------ mapa por recomendacao --------

    st.markdown ('Mapa interativo - recomendacoes de compra')
    #mapa base - folium
    map_ = folium.Map (location=[data_selected['lat'].mean(),data_selected['long'].mean()],
                       default_zoom_start=10)

    #para adicionar marcadores ao mapa. folium adiciona um a um
    marker_cluster = MarkerCluster().add_to(map_)

    for i, row in data_selected.iterrows():
        folium.Marker( [row['lat'], row['long']],
                       popup = 'Price ${0} on: {1}. Features: {2} sqft, {3} bathrooms, {4} bedrooms, Year built: {5}'.
                       format ( row['price'], row['date'], row['sqft_lot'], row['bathrooms'], row['bedrooms'], row['yr_built'])
                      ).add_to(marker_cluster)

        
    folium_static (map_)

    
    return None



def table_buy_recomendation (data_selected):
# ----------tabela de recomendacao------
    st.markdown ('Tabela com recomendações de compra')
    st.write (data_selected)
    
    st.write ('----------------')
    
    return None


# ========================================================================        
# Questao 2 - Uma vez a casa comprada, qual o melhor momento para vendê-las e por qual preço?

def bar_profit_per_quarter (data1):
#     --------- grafico de barras quarter/price_per_sqft---------------------


    st.markdown ('Lucro medio dos imoveis por trimestre')
    
    price_sqft_quarter = data1[['quarter', 'profit']].groupby('quarter').mean().reset_index()
    
    st.bar_chart (data =  price_sqft_quarter,  x= 'quarter' , y= 'profit', use_container_width=True )
    
    return None


def map_sell_recomendation (data1):
#----------- mapa por faixa de preço de compra recomendado e condition ---------------
    
    st.markdown ('Mapa interativo - recomendacoes de venda')
    #mapa base - folium
    map_ = folium.Map (location=[data1['lat'].mean(),data1['long'].mean()],
                       default_zoom_start=10)

    #para adicionar marcadores ao mapa. folium adiciona um a um
    marker_cluster = MarkerCluster().add_to(map_)

    for i, row in data1.iterrows():
        folium.Marker( [row['lat'], row['long']],
                       popup = 'Price ${0} on: {1} - {2}. Selling price recomended: ${3}. Features: {4} sqft, {5} bathrooms, {6} bedrooms, Year built: {7}'.
                       format ( row['price'], row['date'], row['quarter'], row['selling_price_recomended'], row['sqft_lot'], row['bathrooms'], row['bedrooms'], row['yr_built'])
                      ).add_to(marker_cluster)


    folium_static (map_)

    
    return None



def table_sell_recomendation (data1):
    # ----- tabela de recomendacao de preço de venda------ 
    st.markdown ('Tabela com recomendacao de preços de venda')
    st.write(data1)

    st.write ('----------------')

    return None


def table_of_profits(data1):
    
    st.markdown("""
                **Lucros esperados para:** 
                - 1- Preços acima da mediana dos preços da regiao e trimestre: 10% de margem 
                - 2- Preços abaixo da mediana dos preços da regiao e trimestre: 30% de margem 
                
                    *os imoveis selecionados foram aqueles recomendados para compra*
                """)
    data_profit = data1.loc[data1['buy_recomendation']=='buy', ['above_median','profit']]
 
    profit_groupy = pd.DataFrame(data_profit.groupby('above_median').sum().reset_index())    
    profit_groupy['margin_profit'] = profit_groupy['above_median'].apply(lambda x: '10%' if x == 'yes' else '30%')
    
    st.dataframe(profit_groupy)
    
    return None


if __name__ == '__main__':
    
    st.sidebar.markdown('''
    # Questoes de negocio
    - [Questao 1](#questao-1)
    - [Questao 2](#questao-2)
    - [Lucros esperados](#lucros-esperados)
    ''', unsafe_allow_html=True)

    path = 'kc_house_data.csv'
    
    # Load Data
    data = Home.get_data(path)
    
    
    #transformation
    data1 = Home.set_new_features (data)
    
    
    
    ## Questao 1
    st.header ('Questao 1')
    st.subheader ('Recomendações de compra')
    data_selected = filter_recomendation (data1)
    map_buy_recomendation(data_selected)
    table_buy_recomendation (data_selected)
    
    
    ## Questao 2
    st.header('Questao 2')
    st.subheader ('Recomendações de preço de venda')
    bar_profit_per_quarter (data1)
    map_sell_recomendation (data1)
    table_sell_recomendation (data1)
    
    #Lucros esperados
    st.header('Lucros esperados')
    table_of_profits(data1)
    
    
    

  