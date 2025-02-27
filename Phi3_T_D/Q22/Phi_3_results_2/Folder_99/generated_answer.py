def find_sum_of_multiples(number):
    sum_of_multiples = sum((number * i for i in range(1, 421)))
    return sum_of_multiples