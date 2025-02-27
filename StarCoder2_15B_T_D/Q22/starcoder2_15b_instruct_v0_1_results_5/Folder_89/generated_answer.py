def find_sum_of_multiples(number):
    multiples = [i * number for i in range(1, 38)]
    return sum(multiples)