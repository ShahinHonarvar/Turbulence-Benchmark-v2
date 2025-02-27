def find_sum_of_multiples(num):
    multiples = [i * num for i in range(1, 29)]
    return sum(multiples)