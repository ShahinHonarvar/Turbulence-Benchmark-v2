def find_sum_of_multiples(number):
    total_sum = sum((number * i for i in range(1, 476)))
    return total_sum