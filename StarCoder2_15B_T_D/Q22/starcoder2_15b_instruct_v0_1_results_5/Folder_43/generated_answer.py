def find_sum_of_multiples(num):
    multiples_sum = 0
    for i in range(1, 75):
        multiple = num * i
        multiples_sum += multiple
    return multiples_sum