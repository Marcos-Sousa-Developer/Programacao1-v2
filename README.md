<p align="center">
    <img src="https://img2.gratispng.com/20181111/lvr/kisspng-analytics-computer-icons-data-analysis-data-scienc-expertise-fuzion-analytics-5be890d2ca5ab6.4264525715419680828289.jpg" alt="Logo" width="80" height="80">
</p>

# <h1 align="center">Análise de Dados</h3>
<h4 align="center">Projeto para a cadeira de Programação 1 (Parte2) (2020/2021)</h5>

<hr>

# Objetivo
O tema deste projeto é muito relevante no mundo da Informática, sendo usado em áreas como a Prospeção de Dados (em inglês, Data Mining), na compressão de dados, ou em Machine Learning. <br>
Num gráfico de pontos percebemos que existem diferentes aglomerados de pontos. Isto leva-nos à ideia de querer obter estes aglomerados, ou seja, distribuir os pontos dados por diferentes grupos. <br>
Vamos imaginar, por exemplo, que estes dados dizem respeito a clientes de uma empresa, onde o eixo dos xx corresponde ao dinheiro gasto no ano fiscal anterior, e o eixo dos yy ao número de transacções efetuadas (sendo o ponto 0,0 a média destas medidas). Seria interessante criar categorias diferentes de clientes a partir dos aglomerados para que a empresa tivesse estratégias de marketing diferentes para cada categoria. <br>
Há de imediato o problema de saber quantos aglomerados devemos considerar. Estes aglomerados não existem excepto como expressão do modelo que estamos a tentar criar. Convinha ser o computador a dar-nos uma estimativa do melhor número k de aglomerados (até porque se o problema tiver mais de duas dimensões, deixamos de conseguir visualizar os dados) e, quando soubéssemos esse valor de k, classificar os vários clientes pelas respectivas categorias.

<hr>

# Instruções  

## Função criarDados 
Dada uma lista de inteiros ns e uma semente aleatória, gera len(ns) aglomerados, onde o aglomerado i possui ns[i] pontos. A geração dos dados é aleatória mas baseada no valor da semente dada (ou seja, para o mesmo valor de semente são criados sempre os mesmos pontos).

#### **Run it on terminal or open the code (main.py) and test it** 
```bash
python3 -c 'from main import *; print(criarPontos([1,.,.,.,N], "YOUR SEED VALUE")))'
```

## Função distancia 
Dados dois pontos 2D, devolve a sua distância euclidiana.

#### **Run it on terminal or open the code (main.py) and test it** 
```bash
python3 -c 'from main import *; print(distancia( (X1,Y1),(XN,YN) ))'
```

## Função sugerirCentroide 
Vamos assumir que já tomámos a decisão de ter k centróides e temos, de momento, uma lista de candidatos.
Se nos derem um ponto pt dos dados originais, queremos saber qual o centróide mais perto de pt (de acordo com a distância Euclidiana).

#### **Run it on terminal or open the code (main.py) and test it** 
```bash
python3 -c 'from main import *; print(sugerirCentroide([(X1,Y1)...(XN,YN)], (X1,Y1) ))'
``` 
## Função encontrarCentroMassa 
Dado uma lista de pontos 2D devolve um par com as coordenadas do centro de massa destes pontos.

#### **Run it on terminal or open the code (main.py) and test it** 
```bash
python3 -c 'from main import *; print(encontrarCentroMassa([(X1,Y1)...(XN,YN)])'
``` 

## Função aglomerar 
Recebe o número de aglomerados, a lista de pontos, a tolerância máxima que define a convergência do algoritmo e o número máximo de iterações permitidas para o cálculo dos centróides.

#### **Run it on terminal or open the code (main.py) and test it** 
```bash
python3 -c 'from main import *; print(aglomerar("YOUR K VALUE", [(X1,Y1)...(XN,YN)], tol=0.001, maxIter=500))'
``` 

## Função custear 
Recebe uma lista de centróides e a lista com os pontos originais, e devolve a soma dos quadrados das distâncias entre cada ponto e o centróide mais próximo.

#### **Run it on terminal or open the code (main.py) and test it** 
```bash
python3 -c 'from main import *; pts =  criarPontos([(X1,Y1)...(XN,YN)],"YOUR SEED VALUE"); print(aglomerar(2, pts))'
``` 

## Função sugerirK 
Recebe a lista dos pontos iniciais, e dois inteiros que definem o intervalo de procura do valor k

#### **Run it on terminal or open the code (main.py) and test it** 
```bash
python3 -c 'from main import *; pts =  criarPontos([(X1,Y1)...(XN,YN)],"YOUR SEED VALUE"); print(sugerirK(pts))'
``` 


