def find_sum_of_multiples(n):
    sum_multiples = sum((n * i for i in range(1, 29)))
    return sum_multiples