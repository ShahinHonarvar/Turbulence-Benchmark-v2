def find_sum_of_multiples(num):
    multiples = []
    for i in range(1, 86):
        multiple = num * i
        if multiple > 0:
            multiples.append(multiple)
    return sum(multiples)