def find_sum_of_multiples(n):
    sum_of_multiples = sum((n * i for i in range(1, 57)))
    return sum_of_multiples