def find_sum_of_multiples(num):
    sum_of_multiples = 0
    for i in range(1, 473):
        multiple = num * i
        sum_of_multiples += multiple
    return sum_of_multiples