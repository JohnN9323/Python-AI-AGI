numbers = [1,2,3,4]
#using map() to square each number
squared = map(lambda x: x**2,numbers)
#convert the iterator to a list to see the results
print(list(squared))