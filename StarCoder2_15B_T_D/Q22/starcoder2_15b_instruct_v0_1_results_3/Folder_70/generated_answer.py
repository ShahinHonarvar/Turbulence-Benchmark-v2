def find_sum_of_multiples(n):
    multiples = range(1, 402)
    sum_of_multiples = sum((n * m for m in multiples))
    return sum_of_multiples