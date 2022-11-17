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


# PAGINA - Hipoteses

def hypothesis_validation (data1):
    st.title ('Hipoteses de negocio')


    c1, c2 = st.columns ((1,1))
    # Hipotese 1 - Imóveis que possuem vista para água, são 30% mais caros, na média.
    c1.subheader('Hipotese 1 - Imóveis que possuem vista para água, são 30% mais caros, na média.')
    waterfront_view = data1[['waterfront', 'price']].groupby('waterfront').mean().reset_index()

    fig = px.bar(waterfront_view, x='waterfront',y= 'price',text_auto=True)

    c1.plotly_chart(fig,use_container_width=True)

    # Hipotese 2 - Imóveis com data de construção menor que 1955, são 50% mais baratos, na média.
    c2.subheader('Hipotese 2 - Imóveis com data de construção menor que 1955, são 50% mais baratos, na média.')
    data1['after_1955'] = data1['yr_built'].apply(lambda x: '< 1955' if x < 1955 else
                                     '>= 1955' if x >= 1955 else 'na')

    by_after_1955 = data1[['after_1955', 'price']].groupby('after_1955').mean().reset_index()


    fig = px.bar(by_after_1955, x='after_1955',y= 'price',text_auto=True)

    c2.plotly_chart(fig,use_container_width=True)


    c1, c2 = st.columns ((1,1))
    # Hipotese 3 - Imóveis com porão sao 25% mais caros do que imoveis com porao 
    c1.subheader('Hipotese 3 - Imóveis com porão tem o preço/sqft_lot 25% mais caros do que imoveis sem porão.')
    data1['basement'] = data1['sqft_basement'].apply (lambda x: 0 if x>0 else 1)

    by_basement = data1[['price_per_sqft','basement']].groupby('basement').mean().reset_index()

    fig = px.bar(by_basement, x= 'basement', y= 'price_per_sqft',text_auto=True)
    
    c1.plotly_chart (fig, use_container_width=True)


    # Hipotese 4 - O crescimento do preço dos imóveis YoY ( Year over Year ) é de 10%
    c2.subheader('Hipotese 4 - O crescimento do preço dos imóveis YoY ( Year over Year ) é de 10%')
    data1['year'] = pd.to_datetime(data1['date']).dt.strftime('%Y')
    by_year = data1[['year','price']].groupby('year').mean().sort_values('year').reset_index()

    fig = px.bar(by_year, x= 'year', y= 'price',text_auto=True)

    c2.plotly_chart (fig, use_container_width=True)


    c1, c2 = st.columns ((1,1))
    # Hipotese 5 - Imóveis com 3 banheiros tem um crescimento MoM de 15%.
    c1.subheader('Hipotese 5 - Imóveis com 3 banheiros tem um crescimento MoM de 15%.')

    data1['yr_month'] = pd.to_datetime(data1['date']).dt.strftime('%Y-%m')
    by_bathrooms = data1.loc[data1['bathrooms']==3, ['id','yr_month']]
    by_bathrooms = by_bathrooms.groupby('yr_month').count().reset_index()

    total_acumulated = 0 

    for i, line in by_bathrooms.iterrows():

        total_acumulated += line['id']
        by_bathrooms.loc[i,'total_acumulated'] = total_acumulated


    final_value = by_bathrooms.loc[by_bathrooms['yr_month']== by_bathrooms['yr_month'].max(),'total_acumulated']
    initial_value = by_bathrooms.loc[by_bathrooms['yr_month']== by_bathrooms['yr_month'].min(),'total_acumulated']

    
    final_value = pd.DataFrame(final_value).reset_index()
    initial_value = pd.DataFrame(initial_value).reset_index()

    
    final = final_value.loc[0,'total_acumulated']
    initial = initial_value.loc[0,'total_acumulated']

    # growth_rate_avg é o crescimento medio MoM dos imoveis durante o periodo
    growth_rate_avg = (((final/initial)**(1/12))-1)*100

    st.write ('Crescimento medio da base de imoveis com 3 banheiros: {:.2f}%'.format(growth_rate_avg))
    
    
    fig = px.bar(by_bathrooms, x= 'yr_month', y= 'total_acumulated',text_auto=True)

    c1.plotly_chart (fig, use_container_width=True)
    plt.xticks ( rotation = 80 );
    
    return None


if __name__ == '__main__':
    
    path = 'kc_house_data.csv'

    #load data
    data = Home.get_data(path) 
    
    #data transformation 
    data1 = Home.set_new_features(data)
    
#     st.dataframe(data1.head(), width=2000)
    hypothesis_validation (data1)
    