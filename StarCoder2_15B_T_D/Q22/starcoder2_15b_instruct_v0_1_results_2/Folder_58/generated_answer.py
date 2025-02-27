def find_sum_of_multiples(num):
    total = 0
    for i in range(1, 224):
        total += num * i
    return total