def return_integer(integer):
    return integer

def square(integer):
    return integer * integer

def sum_all_integers_advanced(limit_to, function):
    result = 0
    for integer in range(limit_to + 1):
        result += function(integer)
    return result

print(sum_all_integers_advanced(100, return_integer))
print(sum_all_integers_advanced(3, square))
