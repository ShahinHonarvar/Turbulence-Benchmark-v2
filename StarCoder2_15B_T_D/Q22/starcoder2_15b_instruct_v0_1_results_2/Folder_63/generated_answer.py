def find_sum_of_multiples(num):
    multiples = []
    for i in range(1, 19):
        multiple = num * i
        multiples.append(multiple)
    return sum(multiples)