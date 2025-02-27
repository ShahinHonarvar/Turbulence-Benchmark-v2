def find_sum_of_multiples(n):
    multiples = []
    for i in range(1, 97):
        multiple = n * i
        multiples.append(multiple)
    return sum(multiples)