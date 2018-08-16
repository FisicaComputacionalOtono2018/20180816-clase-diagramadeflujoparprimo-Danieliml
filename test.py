
#Author: Daniel Lima Lopez
#Fecha: 16-08-2018
#Ejercicio
s=12

p=input("Ingresa un valor: ")
p2=p
p=0

c=0
o=0

while s!=0:

  while p<s:
   if o==0:
    p=p2
   o=o+1
   while c==0:
     p=p+2
     aux1=p%2

     if aux1==0:
       p=p+1

     i=2
     c=0
     while i<p:
       r=p%i
       if r==0:
         c=1
       i=i+1
     if c==1:
       p=p+2

  s=s-1

print "sale"
print(p)



  
      
      

  
  

  
