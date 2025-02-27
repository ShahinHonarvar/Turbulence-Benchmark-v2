def find_sum_of_multiples(num):
    multiples = []
    for i in range(1, 34):
        multiple = num * i
        multiples.append(multiple)
    return sum(multiples)