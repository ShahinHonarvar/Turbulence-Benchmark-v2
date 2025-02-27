def find_sum_of_multiples(num):
    multiples = []
    for i in range(1, 75):
        multiple = num * i
        multiples.append(multiple)
    sum_of_multiples = sum(multiples)
    return sum_of_multiples