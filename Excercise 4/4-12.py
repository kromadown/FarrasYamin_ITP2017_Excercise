my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print ('My favorite foods are:')
for i in my_foods [:]:
    print (i.title())
print ('My friend’s favorite foods are:')
for i in friend_foods[:]:
    print (i.title())
