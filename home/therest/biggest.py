n = int(input("Enter the size of the array: "))

array = []

print("Enter elements for the array")
for i in range(n):
    element = int(input("Enter element {}".format(i+1)))
    array.append(element)

largest = float('-inf')
second_largest = float('-inf')

for element in array:
    if element > largest:
        second_largest = largest
        largest = element
    elif element > second_largest and element != largest:
        second_largest = element

print("Second largest element is ", second_largest)
