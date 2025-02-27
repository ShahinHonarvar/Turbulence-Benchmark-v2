def find_sum_of_multiples(number):
    multiples = [i for i in range(1, 290) if number * i > 0]
    return sum(multiples)