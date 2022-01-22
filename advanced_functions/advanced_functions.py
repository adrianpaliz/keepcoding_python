def return_integer(integer):
    return integer

def square(integer):
    return integer * integer

def cube(integer):
    return integer**3

def sum_all_integers_advanced(limit_to, function):
    result = 0
    for integer in range(limit_to + 1):
        result += function(integer)
    return result

if __name__ == '__main__':
    print(sum_all_integers_advanced(100, return_integer))
    print(sum_all_integers_advanced(3, square))
    print(sum_all_integers_advanced(3, cube))
