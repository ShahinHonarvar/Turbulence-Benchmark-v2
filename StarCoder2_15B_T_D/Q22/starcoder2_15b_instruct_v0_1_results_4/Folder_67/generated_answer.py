def find_sum_of_multiples(n):
    sum_of_multiples = 0
    num_multiples = 42
    for i in range(1, num_multiples + 1):
        multiple = n * i
        sum_of_multiples += multiple
    return sum_of_multiples