def find_sum_of_multiples(n):
    multiples = []
    for i in range(1, 182):
        multiple = n * i
        multiples.append(multiple)
    return sum(multiples)