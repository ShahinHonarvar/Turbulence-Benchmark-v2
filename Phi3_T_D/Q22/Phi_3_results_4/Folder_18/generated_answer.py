def find_sum_of_multiples(n):
    first_392_multiples = [n * i for i in range(1, 393)]
    return sum(first_392_multiples)