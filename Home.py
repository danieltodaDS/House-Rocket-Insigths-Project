import pandas as pd
import streamlit as st
import numpy as np

# -----------------------------------
# Helper functions
# -----------------------------------
@st.cache (allow_output_mutation = True)
def get_data(path):
    
    data = pd.read_csv (path)
    
    return data


@st.cache (allow_output_mutation = True)
def set_new_features (data): #set_new_features
  
    data1 = data.copy()
    
    # ---datetime
    data1['date'] = pd.to_datetime(data1['date']).dt.strftime('%Y-%m-%d')
    
    
    # ==============================================================================
    # Features for buy recomendation 

    # ---price_per_sqft
    for i in range(len(data1)):
        data1.loc[i, 'price_per_sqft'] = data1.loc[i,'price']/(data1.loc[i,'sqft_lot']+data1.loc[i,'sqft_living'])

    # ---median_price_zipcode
    price_sqft_per_zipcode = data1[['price_per_sqft','zipcode']].groupby('zipcode').median().reset_index()
    price_sqft_per_zipcode.columns=['zipcode','median_price_zipcode']

    data1 = pd.merge(data1,price_sqft_per_zipcode,on='zipcode',how='left')


    # ---buy_recomendation
    for i, line in data1.iterrows():
        if ((line['price_per_sqft']) < (line['median_price_zipcode'])) & (line['condition']>=3):
            data1.loc[i,'buy_recomendation'] = 'buy'
        else:
            data1.loc[i,'buy_recomendation'] = 'not_buy'

            
    # ==============================================================================
    # Features for sell recomendation 

    # ---quarter and price_quarter_zipcode 
    data1['month'] = pd.to_datetime(data1['date']).dt.strftime('%m')

    data1['quarter'] = data1['month'].apply(lambda x: 'Q1' if 1<=int(x)<=3 else
                                                   'Q2' if 4<=int(x)<=6 else
                                                   'Q3' if 7<=int(x)<=9 else
                                                   'Q4' if 10<=int(x)<=12 else 'NA')

    price_quarter_zipcode = data1[['price_per_sqft','quarter','zipcode']].groupby(['quarter','zipcode']).median().reset_index()

    price_quarter_zipcode.columns=['quarter','zipcode','price_quarter_zipcode']

    data1 = pd.merge(data1, price_quarter_zipcode, on = ['quarter','zipcode'], how ='left')

    
    # ---selling_price_recomended, above_median, profit
    for i, line in data1.iterrows():
        if (line['price_per_sqft']>line['price_quarter_zipcode']):
            data1.loc[i,'above_median'] = 'yes'
            data1.loc[i,'selling_price_recomended'] = line['price']*1.1
            data1.loc[i,'profit'] = line['price']*0.1
        else:
            data1.loc[i,'above_median'] = 'no'
            data1.loc[i,'selling_price_recomended'] = line['price']*1.3
            data1.loc[i,'profit'] = line['price']*0.3
            
    
    
    return data1
    
    

def data_view (data1):
    st.header ('Dataset overview')
    x = st.checkbox('Mostre os imoveis a venda em Seattle ')
    if x:

        st.dataframe(data1, width=2000)
    
    return None



def data_describe (data1):
    st.header('Estatistica descritiva dos dados')
    
    num_attributes = data1.select_dtypes (include =['float64','int64'])

    #central tendency
    c1 = pd.DataFrame (num_attributes.apply(np.mean)).T
    c2 = pd.DataFrame (num_attributes.apply(np.median)).T

    #dispersion
    d1 = pd.DataFrame(num_attributes.apply(np.std)).T
    d2 = pd.DataFrame(num_attributes.apply(min)).T
    d3 = pd.DataFrame(num_attributes.apply(max)).T
    d4 = pd.DataFrame(num_attributes.apply(lambda x: x.max() - x.min())).T
    d5 = pd.DataFrame(num_attributes.apply(lambda x: x.skew())).T
    d6 = pd.DataFrame(num_attributes.apply(lambda x: x.kurtosis())).T

    #Concatenate
    descriptive_analysis = pd.concat ([d2, d3, d4, c1, c2, d1, d5, d6]).T.reset_index()
    descriptive_analysis.columns = ['attributes', 'min', 'max', 'range', 'mean', 'median', 'std', 'skew', 'kurtosis']
    
    x = st.checkbox('Mostre as estatisticas descritivas dos atributos dos imoveis')
    if x:
#         st.header('Estatisticas descritivas dos atributos dos imoveis a venda em Seattle ')
        st.dataframe(descriptive_analysis, width=2000)
           
    return None


if __name__ == '__main__':
    
    st.set_page_config(
        page_title='Home',
        page_icon='🏠',
        layout='wide'
    )
    
    st.sidebar.title("Projeto")
    st.sidebar.info(
            "Esse é um projeto desenvolvido nas aulas do curso 'Python do ZERO ao DS'. "         
        )
    st.sidebar.title("Sobre")
    st.sidebar.info(
            """
            Esse projeto é uma analise exploratoria dos dados dos imoveis de King Souty, USA
            com o proposito de responder às perguntas do CEO e obter insights. 
           """
        )
        
    st.markdown("# Bem vindo ao projeto House Rocket! 👋")
    
    st.markdown(
    """
    O projeto House Rocket visa encontrar os imoveis adequados para compra, que maximizem os lucros e encontre
    as melhores oportunidades de negocio
    
    #### Esse projeto de Ciencia de Dados esta interessado em resolver duas questoes elaboradas pelo CEO da House Rocket:
  
      1. Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?
      2. Uma vez comprado o imóvel, qual é o melhor momento para vender e a que preço?
   
   O problema de negocio proposto e a empresa são ficticios
   
   *O dataset utilizado nesse projeto de estudo foi obtido do desafio do kaggle [House Sales in King County, USA](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction)*
"""
)
    st.write('-----------')
    
    path = 'kc_house_data.csv'
    
    #extration 
    data = get_data (path)
    
    #transformation
    data1 = set_new_features (data)

    #visualization
    data_view (data1)
    data_describe(data1)
    
    