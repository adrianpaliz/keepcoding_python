def sum_squares(limit_to):
    result = 0
    for integer in range(limit_to + 1):
        result += integer * integer
    return result

def sum_all_integers(limit_to):
    result = 0
    for integer in range(0, limit_to + 1):
        result += integer
    return result

print(sum_all_integers(100))
print(sum_squares(3))
