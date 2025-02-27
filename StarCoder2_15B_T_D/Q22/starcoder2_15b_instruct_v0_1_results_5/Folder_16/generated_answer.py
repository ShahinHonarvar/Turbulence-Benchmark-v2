def find_sum_of_multiples(n):
    total = 0
    for i in range(1, 256):
        multiple = n * i
        total += multiple
    return total