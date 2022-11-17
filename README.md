# Projeto de insights - House Rocket 

![image](https://user-images.githubusercontent.com/110186368/202519223-73e8de6a-9817-4c23-887b-26e9bab2dc4a.png)


## 1. A House Rocket e o problema de negocio
  
  A House Rocket é uma empresa ficticia do setor imobiliario, cujo modelo de negocio consiste na compra e venda de imoveis de forma a maximizar a geracao de lucro para a empresa. Para isso, utiliza a tecnologia para identificar as melhores oportuinidades de negocio, buscando imoveis em boas condicoes e a baixos preços, e que assim possam ser revendidos a preços superiores no futuro. 
  
  Esse projeto de Ciencia de Dados esta interessado em resolver duas questoes elaboradas pelo CEO da House Rocket:
  
   1. Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?
   2. Uma vez comprado o imóvel, qual é o melhor momento para vender e a que preço?
   
   O dataset utilizado nesse projeto de estudo foi obtido do desafio do kaggle [House Sales in King County, USA](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction)
    
--------------------------------------------------- 
## 2. Data Overview

  O dataset analisado contem os preços dos imoveis de King County, USA, que inclui a cidade de Seattle. Os imoveis desse dataset tiveram a data de venda entre Maio/2014 e Maio/2015  
  
  **Descricao das colunas do dataset original**
  

| Coluna | Descrição |
| :----- | :-------- |
| ID | ID unico para cada imovel vendido |
| date | Data da venda |
|price | Preço de cada imovel vendido |
|bedrooms | Numero de quartos|
|bathrooms | Numero de banheiros|
|sqft_living | Area interna em pes quadrados|
|sqft_lot | Area externa em pes quadrados|
|floors | Numero de andares|
|waterfront | Vista para agua|
|view | Escala de 0 a 4 que descreve a qualidade da vista do imovel|
|condition | Escala de 1 a 5 que avalia a condicao de conservacao do imovel|
|grade | Escala de 1 a 13 que avalia a qualidade da construcao e design do imovel|
|sqft_above | Area do andar superior do imovel em pes quadrados|
|sqft_basement | Area do porao em pes quadrados|
|yr_built | Ano de construcao do imovel|
|yr_renovated | Ano de reforma do imovel|
|zipcode | Zipcode do imovel, ou endereço postal|
|lat | Latitude|
|long | Longitude|
|sqft_living15 | Area interna em pes quadrados dos 15 imoveis mais proximos|
|sqft_lot15 | Area externa em pes quadrados dos 15 imoveis mais proximos|

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
      
### 4.2. Ferramentas
  - Python 3.8.13, Pandas, Matplotlib, Plotly, Plotly Express, folium e Seaborn
  - Jupyter notebook
  - Streamlit e Streamlit Cloud
  - Git e Github

### 4.3. Processo de solucao

**Questao 1: Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?**

  Para responder essa questao, foram investigados os imoveis que possuiam estado de conservação acima da media e com preço subvalorizado. 
  
  Assim, calculou-se o preço/area dos imoveis, assim como a mediana dos preços/area agrupados por zipcode e foi utilizado a seguinte regra para a recomendacao de compra dos imoveis: 

   - 'condition' >= 3 (condicão acima da media) e
   - preço/area do imovel < mediana dos preços/area agrupado por zipcode

  Assim, foram selecionados os imoveis que tinha boas condicoes de conservacao e que tivessem seus preços abaixo da mediana da regiao



**Questao 2: Uma vez comprado o imóvel, qual é o melhor momento para vender e a que preço?**

  O melhor momento para a venda foi definido com sendo o trimestre em que se observou o maior lucro medio potencial, sendo esses lucro calculado a partir da seguinte regra:
  
  - preço/area do imovel > mediana dos precos/area de mesmo zipcode/trimestre: margem de lucro recomendada 10%
  - preço/area do imovel > mediana dos precos/area de mesmo zipcode/trimestre: margem de lucro recomendada 30%
     
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

Para o calculo dos impactos financeiros desse projeto considerou-se a seleção dos imoveis recomendados para compra e seus preços de venda sugeridos, dado uma margem de lucro estabelecida a partir da mediana dos preços/area dos imoveis adquiridos no mesmo trimestre e no mesmo zipcode. 

**Dessa forma, chegou-se a um lucro total projetado de R$ 1.506.438.582 na venda dos 10620 imoveis (que foram recomendados para compra), sendo uma media de lucro de R$ 141849 por imovel vendido**

-------------------------------

## 7. Conclusoes

Com o projeto foi possivel responder as duas questoes de negocio propostas, assim como apresentar 5 insights obtidos na analise exploratoria dos dados. Todos os resultados estao disponiveis no app House Rocket App. 

----------------------------------

## 8. Proximos passos


-----------------------------------
# Contato 
hiroshi1991@gmail.com
LINKEDIN

