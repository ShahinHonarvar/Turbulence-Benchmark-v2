def find_sum_of_multiples(num):
    total = 0
    for i in range(1, 64):
        multiple = num * i
        total += multiple
    return total