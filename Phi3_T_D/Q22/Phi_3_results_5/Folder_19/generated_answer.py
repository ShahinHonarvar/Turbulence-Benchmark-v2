def find_sum_of_multiples(n):
    sum = 0
    for multiple in range(1, 47):
        sum += n * multiple
    return sum