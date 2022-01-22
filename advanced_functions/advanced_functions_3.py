from functools import reduce

def double(integer):
    return integer + integer

integers_list = [1, 3, -1, 15, 9, 44]

doubles_list_lambda = map(lambda argument : argument * 2, integers_list)
doubles_list = map(double, integers_list)

def is_pair(integer):
    return integer % 2 == 0

pairs_list_lambda = filter(lambda argument : argument % 2 == 0, integers_list)
pairs_list_function = filter(is_pair, integers_list)

summation_lambda = reduce(lambda argument_0, argument_1 : argument_0 + argument_1, integers_list)
summation_doubles = reduce(lambda argument_0, argument_1 : argument_0 + argument_1 * 2, integers_list)

addition_100 = reduce(lambda arg_0, arg_1 : arg_0 + arg_1, range(101))

print(list(doubles_list_lambda))
print(list(doubles_list))
print(list(pairs_list_lambda))
print(list(pairs_list_function))
print(summation_lambda)
print(summation_doubles)
print(addition_100)