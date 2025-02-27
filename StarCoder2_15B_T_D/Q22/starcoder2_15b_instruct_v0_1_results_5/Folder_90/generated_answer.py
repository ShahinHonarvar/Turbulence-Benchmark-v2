def find_sum_of_multiples(n):
    multiples = []
    for i in range(1, 321):
        if n * i > 0:
            multiples.append(n * i)
    return sum(multiples)