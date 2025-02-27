def find_sum_of_multiples(n):
    multiples = range(1, 98)
    return sum((n * i for i in multiples))