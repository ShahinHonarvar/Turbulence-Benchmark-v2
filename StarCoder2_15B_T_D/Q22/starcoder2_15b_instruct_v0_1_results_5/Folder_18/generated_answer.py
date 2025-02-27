def find_sum_of_multiples(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError('Input must be a positive integer.')
    multiples_sum = 0
    for i in range(1, 393):
        multiple = n * i
        multiples_sum += multiple
    return multiples_sum