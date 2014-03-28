import sys

PI=3.14159265358979323846264338327950288

def aproximacion (n):
  suma=0

  for i in range (1,n+1):
    a=(i-1)/float(n)
    b=(i)/float(n)
    xi = (i-0.5)/float(n)
    fxi = (4/(1+xi**2))
    #print "x_i: %f" % (xi)
    #print "fxi: %f" % (fxi)
    #print "a: %f" %(a)
    #print "b: %f" %(b)
    suma = suma + fxi
  pi= suma / float (n)
  #print "pi: %.35f" % (pi)
  #print "El numero PI con 35 decimales es %.35f" % (PI)
  return pi
  
if __name__ == "__main__":
  
 
  if len (sys.argv) !=3:
    print 'faltan los argumentos del programa'
    n=5
    parametro2=5
  else:
    n = int(sys.argv[1])
    parametro2 = int(sys.argv[2])
    
  lista = []
  for i in range (0,parametro2):
    pi = aproximacion(n)
    lista.append(pi)
  print lista    