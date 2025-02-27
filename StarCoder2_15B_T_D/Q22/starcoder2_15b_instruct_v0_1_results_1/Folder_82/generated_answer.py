def find_sum_of_multiples(number):
    multiples = []
    for i in range(1, 34):
        multiple = number * i
        multiples.append(multiple)
    return sum(multiples)