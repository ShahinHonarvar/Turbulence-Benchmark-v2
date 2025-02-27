def find_sum_of_multiples(num):
    limit = 416
    return sum((num * i for i in range(1, limit + 1)))