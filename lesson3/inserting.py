numbers = [4, 6, 2, 9, 3]
print(numbers)

numbers.append(7) # pushing
print(numbers)

newList = [6, 8]

numbers.extend(newList) # merging
print(numbers)

numbers.append(newList) # just push array into array
print(numbers)

numbers.pop() # remove last and return it
print(numbers)

numbers.remove(6) # removes first 6 element from list
print(numbers)
