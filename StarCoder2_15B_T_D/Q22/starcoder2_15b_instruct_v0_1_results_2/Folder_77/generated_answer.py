def find_sum_of_multiples(num):
    total_sum = 0
    for i in range(1, 174):
        multiple = num * i
        total_sum += multiple
    return total_sum