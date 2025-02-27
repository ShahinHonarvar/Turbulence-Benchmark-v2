def find_sum_of_multiples(num):
    multiples = []
    for i in range(1, 367):
        if num * i > 0:
            multiples.append(num * i)
    return sum(multiples)