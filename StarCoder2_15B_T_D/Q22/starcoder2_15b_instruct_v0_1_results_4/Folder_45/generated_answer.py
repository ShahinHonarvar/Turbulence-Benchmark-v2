def find_sum_of_multiples(n):
    multiples = range(1, 73)
    return sum((n * multiple for multiple in multiples))