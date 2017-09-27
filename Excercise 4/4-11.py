pizzas = ['pepperoni','cheese','mayo']
friend_pizzas = pizzas[:]

pizzas.append('chicken')
friend_pizzas.append('sausage')

print ('My favorite pizzas are:')
for i in pizzas [:]:
    print (i.title())
print ('My friend’s favorite pizzas are:')
for i in friend_pizzas[:]:
    print (i.title())
