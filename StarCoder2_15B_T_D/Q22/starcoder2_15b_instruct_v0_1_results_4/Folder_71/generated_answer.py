def find_sum_of_multiples(num):
    multiples = []
    for i in range(1, 17):
        multiples.append(num * i)
    return sum(multiples)