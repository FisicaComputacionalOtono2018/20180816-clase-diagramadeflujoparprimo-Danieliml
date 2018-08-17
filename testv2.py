
#Author: Daniel Lima Lopez
#Fecha: 16-08-2018
#Ejercicio


s=12

p=input("Ingresa un valor: ")
p2=p
p=p-2

i=0
j=0
k=0
auxp=0
aux2=0

while s!=0:
  p2=p
  p=0
  j=0

  while p<s:
    if j==0:
      p=p2
    if j!=0:
      s=s-p
    p=p+2
    k=0
    auxp=0
    while auxp==0:
      if k!=0:
        p=p+2
      aux2=p%2
      if aux2==0:
        p=p+1
      t=2
      auxp=1
      if p>2:
        while t<p:
          aux3=p%t
          if aux3==0:
            auxp=0
          t=t+1
      k=k+1      
    j=j+1
  s=s-1

print"P = "
print(p)
  
      
      

  
  

  
