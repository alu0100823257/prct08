#! /usr/bin/python
#! encoding: UTF-8
import prct07a


def error( n , v, umbral):

  errores = 0.0
  for i in range(v):

    aprox1 = prct07a.aproximacion(n)

    valor = aprox1 - prct07a.PI
    if(abs(valor)>=umbral):

      errores +=1
    return (errores/v)*100

  
if (__name__=="__main__"):

  import sys
  if((len(sys.argv) == 1) or (len(sys.argv) == 2) or (len(sys.argv) == 3)):

    print"No ha introducido los argumentos necesarios, usaremos los estandar, que son 100 intervalos, 10 repeticiones y 0,00001 como umbral"

    n = 100
    v = 10
    umbral = 0.00001
  else:
    n = int(sys.argv[1])

    v = int(sys.argv[2])

    umbral = float(sys.argv[3])

  print error(n, v, umbral)

