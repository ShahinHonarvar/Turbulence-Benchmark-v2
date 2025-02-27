def find_sum_of_multiples(n):
    multiples = []
    for i in range(1, 465):
        multiple = n * i
        if multiple > 0:
            multiples.append(multiple)
    return sum(multiples)