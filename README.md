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

  - *Premissa1.* A localizacao dos imoveis é uma variavel fortemente correlacionada ao preço dos imoveis
  - *Premissa2.* O periodo do ano em que o imovel é adquirido exerce influencia sobre a variabilidade do seu preço. A granularidade escolhida foi o 'trimestre' para os periodos que contemplam um ano. 
  
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
  
  Assim, primeiramente foi derivada a variavel 'price_per_sqft' representando uma metrica de comparação dos preços dos imoveis (preço/area). Em seguida, partindo da premissa que as regioes (zipcode) dos imoveis influenciam sobremaneira o seu preço, foi calculado o 'median_price_zipcode' que representa a mediana dos 'price_per_sqft' de cada um dos zipcode do dataset. A escolha da mediana, como medida de tendencia central, visou tirar a influencia dos outliers dessa analise. 
  
  Com esses valores de 'median_price_zipcode' foram definidos os imoveis recomendados para compra, seguindo as seguintes regras:
    
   - imoveis com 'condition' >= 3
   - imoveis com 'price_per_sqft' < 'median_price_zipcode'

  Assim, foram selecionados os imoveis que tinha boas condicoes de conservacao e que tivessem seus preços abaixo da mediana da regiao


**Questao 2: 2. Uma vez comprado o imóvel, qual é o melhor momento para vender e a que preço?**

  Para responder essa questao foi investigado:
    - qual o periodo do ano (trimestre) em que os preços foram superiores na media. 
    - qual margem de lucro recomendado para cada imovel. 
    
   O periodo do ano com maior preço na media foi calculado a partir dos preços/area medio ('price_per_sqft') dos imoveis agrupados por trimestres ('quarter'). Como o preço praticado nesse periodo foi maior em relacao aos outros, entende-se que ha uma maior chance de efetuar uma nova venda com margens de lucro desejadas e, portanto, recomenda-se a venda nesse periodo
   
   Considerando, alem do periodo em que o imovel foi adquirido, a sua regiao como premissas de negocio que influenciam o preço, foi calculado a mediana dos preços dos imoveis agrupados primeiro por trimestre e depois por 'zipcode', resultando em 'price_quarter_zipcode'. Esse calculo teve como parametro a variavel 'quarter' (trimestre) derivada anteriormente. 
   
   Com base na mediana desses preços agrupados por trimestre, depois por zipcode, decidiu-se sobre o preço de venda recomendado, a partir da regra:
   
   - 'price_per_sqft' > 'price_quarter_zipcode': margem de lucro recomendada 10%
   - 'price_per_sqft' < 'price_quarter_zipcode': margem de lucro recomendada 30%

  Assim, imoveis que foram adquiridos a um preço menor que a mediana dos preços praticados naquele mesmo trimestre (de qualquer ano), de uma mesma regiao, teriam uma margem de lucro recomendada superior aos que foram adquiridos acima dessa mediana. 
   
   
---------------------------------------------------   

## 5. Insights de negocio

### 5.1. Imoveis com vista para agua sao 212% mais caros na media que os que nao possuem essa caracteristica. 
![image](https://user-images.githubusercontent.com/110186368/202251304-bf288f0c-048f-4b6b-b1b3-47de8c3570de.png)

Uso: imoveis com vista para agua, e com preço muito desvalorizado por conta de outros atributos, podem resultar em uma boa margem de lucro se reformados e revendidos posteriormentes


### 5.2. Imoveis com data de construcao após 1955 são aproximadamente 1% mais caros na media em relação aos construidos em periodo anterior
![image](https://user-images.githubusercontent.com/110186368/202255520-5cd32f79-a49b-4e15-b787-5cf0c4b13f48.png)

Uso: essa segmentação nao trouxe impacto significativo para decisoes de negocio


### 5.3. Imoveis sem porao sao 39% mais caros que imoveis com porao, na media
![image](https://user-images.githubusercontent.com/110186368/202283522-00fcbf86-bb01-4a98-a842-e9f09a998926.png)

Uso: Ter porao nao incrementa valor ao imovel e nao deve influenciar a decisao de compra de novos imoveis e nem reforma para se construir poroes nas casas que nao possuem esse atributo

### 5.4. O preço medio dos imoveis de 2015 foram 0,5% superiores aos imoveis do ano anterior
![image](https://user-images.githubusercontent.com/110186368/202285638-944c7a12-064b-439b-9467-f9211cf2ed28.png)

Uso: esse valor pode ser usado como referencia minima para margem de lucro na venda de imoveis, dado que os dados evidenciam que pode haver uma valorizacao YoY 

### 5.5. A base de imoveis com 3 banheiros teve um crescimento medio Mom de 21,89% 

![image](https://user-images.githubusercontent.com/110186368/202294769-666aa06b-85a4-4656-be4a-d8a7218e91b6.png)

Uso: Dada a tendencia positiva de quantidade de imoveis comprados/vendidos com 3 banheiros, mes contra mes, adquirir um imovel com essa caracteristica pode representar um menor risco de vacancia e de liquidez. 


-----------------------------

## 6. Resultados financeiros do projeto para o negocio





## 7. Conclusoes

## 8. Proximos passos

