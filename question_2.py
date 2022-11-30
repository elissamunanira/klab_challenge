item = [ {'name': 'Bike', 'price':100}, 
{'name': 'TV', 'price':200},
{'name': 'Album', 'price':10}, 
{'name': 'Book', 'price':5}, 
{'name': 'Phone', 'price':500}, 
{'name': 'Computer', 'price':1000} 
]

#q1

max=item[0]['price']
for n in range(0,len(item)):
  r=item[n]['price']
  if r <=max:
    max=item[n]['price']
    product=item[n]
print(product)

#q2


max=item[0]['price']
for n in range(0,len(item)):
  r=item[n]['price']
  if r >=max:
    max=item[n]['price']
    product=item[n]
print(product)

#  q3
  
sum=0 
for n in range(0,len(item)):
  sum=sum+item[n]['price']
print(sum)


#------q4
sum=0 
for n in range(0,len(item)):
    if item[n]['price']<10:
        item[n]['price']=0
    sum=sum+item[n]['price']
  
print(sum)