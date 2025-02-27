def find_sum_of_multiples(n):
    multiples = []
    for i in range(1, 42):
        multiple = n * i
        multiples.append(multiple)
    sum_of_multiples = sum(multiples)
    return sum_of_multiples