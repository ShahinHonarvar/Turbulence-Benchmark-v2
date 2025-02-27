def find_sum_of_multiples(num):
    total_sum = 0
    for i in range(1, 92):
        total_sum += num * i
    return total_sum