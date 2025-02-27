def find_sum_of_multiples(number):
    sum_multiples = sum((number * i for i in range(1, 17)))
    return sum_multiples