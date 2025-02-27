def find_sum_of_multiples(number):
    multiples = [i * number for i in range(1, 26)]
    return sum(multiples)