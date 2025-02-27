def find_sum_of_multiples(num):
    sum = 0
    for i in range(1, 50):
        multiple = num * i
        sum += multiple
    return sum