def find_sum_of_multiples(n):
    multiples_sum = 0
    for i in range(1, 117):
        multiple = n * i
        multiples_sum += multiple
    return multiples_sum