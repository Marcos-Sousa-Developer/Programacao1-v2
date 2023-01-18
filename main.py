import matplotlib.pyplot as plt
import numpy as np

def criarDados(k, ns, mus, covs, seed=-1):
  """
  k    : número de aglomerados
  ns   : lista com os tamanhos de cada aglomerado
  mus  : lista dos centros de cada aglomerado
  covs : lista com as matrizes de covariância
  seed : valor para controlar a aleatoriadade (default -1 -> imprevísivel)
  
  retorna uma lista de pares com coordenadas (x,y)
  """
  if seed != -1:
    np.random.seed(seed)
  xs = []
  ys = []
  for i in range(k):
    x,y = np.random.multivariate_normal(mus[i], covs[i], ns[i]).T
    xs.extend(x)
    ys.extend(y)
  
  return (xs,ys)

def criarPontos(ns, seed=-1):
  """
  requires: len(ns) < 8
  """
  k    = len(ns)
  mus  = [[0, 0], [5,5], [4,-5],[-5,-5],[-4,5],[-7.5,0],[0,8]]
  covs = [
      [[2,    0], [    0,  2]],
      [[1, -0.5], [ -0.5,  1]],
      [[2, 0.75], [ 0.75, .5]],
      [[2, 0.75], [ 0.75, .5]],
      [[2,-0.75], [-0.75,  1]],
      [[1, -0.5],  [-0.5,  1]],
      [[1, -0.5], [ -0.5,  1]],
    ]

  x,y = criarDados(k, ns[:k], mus[:k], covs[:k], seed)
  pts = [ (x[i],y[i]) for i in range(len(x))]
  return pts


pts = criarPontos([140, 50, 100, 160, 120], 101)

##for pt in pts:
##  plt.scatter(pt[0], pt[1], marker=".", color='k')
##plt.show()

def distancia(pt1, pt2):

    Xa = pt1[0]
    Ya = pt1[1]
    Xb = pt2[0]
    Yb = pt2[1]

    X = (Xb - Xa) ** 2
    Y = (Yb - Ya) ** 2

    D = (X + Y) ** (1/2)

    return D

#print(distancia((0.0,3.0), (4.0,0.0)))


def sugerirCentroide(centros, pt):
  #retorna a posicao do centroide com menor distancia

    distanceList = list()

    for i in range(len(centros)):

        D = distancia(centros[i],pt)

        distanceList.append(D)

    centroideCloser = distanceList.index(min(distanceList))

    return centroideCloser

##centroides = [(10,10), (20,10), (0,0)]
##print(sugerirCentroide(centroides, (4,4)))
##
##
##centroides = [(10,10), (0,0)]
##print(sugerirCentroide(centroides, (5,5)))

def encontrarCentroMassa(pts):

#O centro de massa é um ponto que se comporta como
#se toda a massa estivesse
#concentrada sobre ele (o centro).
    x = 0
    y = 1

    massa = 0
    countX = 0
    countY = 0
    for i in range(len(pts)):

        countX += pts[i][x]
        countY += pts[i][y]
        massa +=1
    

    xCM = countX / massa
    yCM = countY / massa

    centroMassa = (xCM,yCM)

    return centroMassa

##print(encontrarCentroMassa([(0,0),(6,6),(0,6)]))
##
##lista = []
##for i in range(100):
##  pts = criarPontos([100,150], i)
##  lista.extend(encontrarCentroMassa(pts))
##print(round(sum(lista),3))

def aglomerar(k, pts, tol=0.001, maxIter=500):
    # o k refere-se ao número de centoroides

    count = 0

    primeiros_k_centroides = dict()
    #criar um dicionário para com respetivas chaves coordenas centroide
    for i in range(k):
        primeiros_k_centroides[pts[i]] = []
        
    centros = list()
    #lista com as coordendas das centroides
    for i in range(k):
        centros.append(pts[i])
    
    while count < maxIter:
        
        #adicionar na respetivo dicionario e respetiva chaves os pontos
        # de acordo com a sugestão
        for ponto in pts:
            posicao = sugerirCentroide(centros,ponto)
            primeiros_k_centroides[centros[posicao]].append(ponto)
        
        centroideList = list()
        #criação do centro massa
        for centro in centros:
            centroMassa = encontrarCentroMassa(primeiros_k_centroides[centro])
            centroideList.append(centroMassa)

        dist = 0
        for i in range(len(centros)):
            
            dist += distancia(centroideList[i],centros[i])

        if dist < tol:
            return centroideList

        else:
            
            centros = list()
            primeiros_k_centroides = dict()
            for i in range(k):
                primeiros_k_centroides[centroideList[i]] = []
                centros.append(centroideList[i])
               
        count +=1

    return centroideList


##pts = criarPontos([140, 50, 100, 160, 120], 101)
##centros = aglomerar(1, pts)
##print([ (round(x,2),round(y,2)) for (x,y) in centros ])

##pts = criarPontos([140, 50, 100, 160, 120], 101)
##centros = aglomerar(2, pts)
##centros.sort()
##print([ (round(x,2),round(y,2)) for (x,y) in centros ])

def custear(centros, pts):

  centroides = dict()

  for centro in centros:

    centroides[centro] = []

  for ponto in pts:

    posicao = sugerirCentroide(centros, ponto)

    centroides[centros[posicao]].append(ponto)

  soma = 0
  for centro in centros:
    for i in range(len(centroides[centro])):
      dist = distancia(centro,centroides[centro][i])
      soma += dist**2

  return soma
      
##pts = criarPontos([140, 50, 100, 160, 120], 101)
##centros = aglomerar(2, pts)
##print(round(custear(centros, pts),3))
##
##pts = criarPontos([140, 50, 100, 160, 120], 101)
##centros = aglomerar(4, pts)
##print(round(custear(centros, pts),3))


def sugerirK(pts, minK=2, maxK=10):

  Ks = dict() #dicionario de Ks com respetivo centros
  finalKs = dict() #dicionario com o número de custo

  for k in range(minK,maxK+1):

    Ks[k] = []
    finalKs[k] = []

  for k in Ks:

    Ks[k].append(aglomerar(k, pts)) #criar determinados centroides de acordo com o numero de ks
    finalKs[k].append(custear(Ks[k][0],pts) * k**1.5) #calculo do custo

  custo = dict() 
  minCusto = list() #lista com as contas do custo

  count = minK
  for k in finalKs:
    custo[finalKs[k][0]] = count #inverter o dicionario k passam a ser os valores
    count += 1
    minCusto.append(finalKs[k][0]) #lista com as contas do custo

  return custo[min(minCusto)]


##
##pts = criarPontos([140, 50, 100, 160, 120], 101)
##k = sugerirK(pts)
##print(k)

  

    



    

    


