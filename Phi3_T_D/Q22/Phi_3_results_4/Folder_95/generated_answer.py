def find_sum_of_multiples(n):
    multiples_sum = sum((n * i for i in range(1, 89)))
    return multiples_sum