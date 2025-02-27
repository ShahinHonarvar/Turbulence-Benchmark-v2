def find_sum_of_multiples(n):
    if n <= 0:
        return 0
    sum_of_multiples = sum((n * i for i in range(1, 34)))
    return sum_of_multiples