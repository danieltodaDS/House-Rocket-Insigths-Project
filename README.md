# Projeto House Rocket


## 1. A House Rocket e o problema de negocio
  
  A House Rocket é uma empresa ficticia do setor imobiliario, cujo modelo de negocio consiste na compra e venda de imoveis de forma a maximizar a geracao de lucro para a empresa. Para isso, utiliza a tecnologia para identificar as melhores oportuinidades de negocio, buscando imoveis em boas condicoes e a baixos preços, e que assim possam ser revendidos a preços superiores no futuro. 
  
  Esse projeto de Ciencia de Dados esta interessado em resolver duas questoes elaboradas pelo CEO da House Rocket:
    1. Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?
    2. Uma vez comprado o imóvel, qual é o melhor momento para vender e a que preço?
    
--------------------------------------------------- 
## 2. Data Overview

  O dataset analisado contem os preços dos imoveis de King County, USA, que inclui a cidade de Seattle. Os imoveis desse dataset tiveram a data de venda entre Maio/2014 e Maio/2015  
  
  **Descricao das colunas do dataset original** 
  
    fonte: https://www.kaggle.com/datasets/harlfoxem/housesalesprediction/discussion/207885

| Coluna | Descrição |
| :----- | :-------- |
| ID | Unique ID for each home sold |
| date | Date of the home sale |
| price | Price of each home sold |
|bedrooms | Number of bedrooms|
|bathrooms | Number of bathrooms, where .5 accounts for a room with a toilet but no shower|
|sqft_living | Square footage of the apartments interior living space|
|sqft_lot | Square footage of the land space|
|floors | Number of floors|
|waterfront | A dummy variable for whether the apartment was overlooking the waterfront or not|
|view | An index from 0 to 4 of how good the view of the property was|
|condition | An index from 1 to 5 on the condition of the apartment,|
|grade | An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design.|
|sqft_above | The square footage of the interior housing space that is above ground level|
|sqft_basement | The square footage of the interior housing space that is below ground level|
|yr_built | The year the house was initially built|
|yr_renovated | The year of the house’s last renovation|
|zipcode | What zipcode area the house is in|
|lat | Lattitude|
|long | Longitude|
|sqft_living15 | The square footage of interior housing living space for the nearest 15 neighbors|
|sqft_lot15 | The square footage of the land lots of the nearest 15 neighbors|

--------------------------------------------------- 
## 3. Premissas de negocio 

  - Como premissa, considerou-se a localizacao dos imoveis como uma variavel fortemente correlacionada ao preço dos imoveis

--------------------------------------------------- 
## 4. Planejamento da solucao 

### 4.1. Produto final
  - Solucao para Questao 1:
    - Tabela com recomendacao de compra: contem os imoveis filtrados entre as opcoes do Filtro de recomendação 
    - Mapa interativo: contem os imoveis e seus atributos filtrados entre as opcoes do Filtro de recomendação
    - Filtro de recomendação, contem as opções "Recomendado", "Nao recomendado" e "Todos". 

  - Solucao para Questao 2: 
    - Tabela com recomendacao de venda: contem trimestre de aquisicao, preço de venda e lucro recomendado
    - Mapa interativo: contem localizacao dos imoveis, seus atributos e preço recomendado de venda
  
  - FINANCIAL RESULTS
    
### 4.2. Ferramentas
  - Python 3.8.13, Pandas, Matplotlib, Plotly, Plotly Express, folium e Seaborn
  - Jupyter notebook
  - Streamlit 
  - Heroku 
  - Git e Github

### 4.3. Processo de solucao

**Questao 1: Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?**

  Para responder essa questao, foram investigados os imoveis que possuiam estado de conservação acima da media e com preço subvalorizado. 
  
  Assim, primeiramente foi derivada a variavel 'price_per_sqft' representando uma metrica de comparação dos preços dos imoveis (preço/area). Em seguida, partindo da premissa que as regioes (zipcode) dos imoveis influenciam sobremaneira o seu preço, foi calculado o 'price_sqft_per_zipcode' que representa a mediana dos 'price_per_sqft' de cada um dos zipcode do dataset. A escolha da mediana, como medida de tendencia central, visou tirar a influencia dos outliers dessa analise. 
  
  Com esses valores de 'price_sqft_per_zipcode' foram definifos os imoveis recomendados para compra, seguindo as seguintes regras:
    
   - imoveis com 'condition' >= 3
   - imoveis com 'price_per_zipcode' < 'price_sqft_per_zipcode'

  Assim, foram selecionados os imoveis que tinha boas condicoes de conservacao e que tivessem seus preços abaixo da mediana da regiao

**Questao 2: 2. Uma vez comprado o imóvel, qual é o melhor momento para vender e a que preço?**

---------------------------------------------------   
## 5. Analise das hipoteses de negocio 

## 6. Resultados financeiros do projeto para o negocio 

## 7. Conclusoes

## 8. Proximos passos

