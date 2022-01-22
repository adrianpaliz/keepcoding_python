def return_maximum_value(*array):
    if len(array) == 0:
        return 0
    maximum_value = array[0]
    for index in range(1, len(array)):
        if array[index] > maximum_value:
            maximum_value = array[index]
    return maximum_value

def return_minimum_value(*array):
    if len(array) == 0:
        return 0
    minimum_value = array[0]
    for index in range(1, len(array)):
        if array[index] < minimum_value:
            minimum_value = array[index]
    return minimum_value

def return_middle_value(*array):
    if len(array) == 0:
        return 0
    addition = 0
    for value in array:
        addition += value
    return addition / len(array)

print(return_maximum_value(1, 3, -1, 15, 9))
print(return_minimum_value(1, 3, -1, 15, 9, 8))
print(return_middle_value(1, 3, -1, 15, 9, 21, 6))

functions = {
    'max' : return_maximum_value,
    'min' : return_minimum_value,
    'med' : return_middle_value
    }

def return_function(name):
    name = name.lower()
    if name in functions.keys():
        return functions[name]
    return None

print(return_function('max')(1, 3, -1, 15, 9))
print(return_function('min')(1, 3, -1, 15, 9, 8))
print(return_function('med')(1, 3, -1, 15, 9, 21, 6))
