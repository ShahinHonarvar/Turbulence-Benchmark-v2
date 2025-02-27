def find_sum_of_multiples(num):
    sum_of_multiples = sum((num * i for i in range(1, 38)))
    return sum_of_multiples