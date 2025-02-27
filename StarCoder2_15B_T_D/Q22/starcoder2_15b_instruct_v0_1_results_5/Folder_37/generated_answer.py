def find_sum_of_multiples(num):
    multiples = []
    for i in range(1, 18):
        multiples.append(i * num)
    return sum(multiples)