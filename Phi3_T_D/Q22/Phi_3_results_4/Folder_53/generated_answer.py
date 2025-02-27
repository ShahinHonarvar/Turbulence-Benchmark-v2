def find_sum_of_multiples(n):
    if n <= 0:
        return 0
    multiples_sum = sum((n * i for i in range(1, 61)))
    return multiples_sum