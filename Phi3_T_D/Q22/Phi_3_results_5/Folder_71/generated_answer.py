def find_sum_of_multiples(n):
    target_count = 16
    sum_multiples = sum((n * i for i in range(1, target_count + 1)))
    return sum_multiples