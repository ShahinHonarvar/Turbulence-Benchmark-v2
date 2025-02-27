def find_sum_of_multiples(num):
    multiples = [i * num for i in range(1, 207)]
    return sum(multiples)