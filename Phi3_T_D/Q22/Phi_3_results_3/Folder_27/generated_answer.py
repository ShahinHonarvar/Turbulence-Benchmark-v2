def find_sum_of_multiples(n):
    sum_ = 0
    for i in range(1, 55):
        sum_ += n * i
    return sum_