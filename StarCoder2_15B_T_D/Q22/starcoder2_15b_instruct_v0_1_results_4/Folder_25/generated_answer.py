def find_sum_of_multiples(num):
    multiples = [i * num for i in range(1, 35)]
    return sum(multiples)