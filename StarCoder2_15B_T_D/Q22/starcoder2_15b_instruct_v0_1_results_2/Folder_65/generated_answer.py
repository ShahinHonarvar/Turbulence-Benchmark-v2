def find_sum_of_multiples(number):
    multiples_sum = 0
    for i in range(1, 81):
        multiple = number * i
        multiples_sum += multiple
    return multiples_sum