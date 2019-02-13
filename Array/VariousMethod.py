fruits = ['apple', 'banana', 'cherry', 'orange']
flowers= ['Rose','Lotus','Jasmin']
points = (1, 4, 5, 9)

#fruits.clear()
#print(fruits)

x = fruits.copy()   #copy
print(x)

y = fruits.count('banana')      #count element
print(y)

fruits.extend(flowers)       #add whole array end to the first array
print(fruits)

flowers.extend(points)
print(flowers)

