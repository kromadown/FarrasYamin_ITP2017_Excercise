towns = ['Jakarta', 'Bandung', 'Surabaya', 'Bali', 'Denpasar']
colors = ['red','blue','yellow','green']
numbers = [1,2,3,4,5]

print ('I love ' + towns[0])
print ('But I prefer ' + towns[3])
print ('I like ' + colors[1])

print ("I don't really like yellow actually, but black is good")
del colors[2]
colors.append('black')
print ('So my fav colors are ' + str(colors))

numbers.insert(5, 6)
print ('After 5 is ' + str(numbers[5]))

nope = towns.pop(4)
print ('But ' + nope + ' is too far')

del (towns[1])
print (towns)

print (sorted(colors))
print (sorted(colors, reverse=True))
colors.reverse()
print (colors)
towns.sort()
print (towns)
towns.sort(reverse=True)
print (towns)
print(len(numbers))
