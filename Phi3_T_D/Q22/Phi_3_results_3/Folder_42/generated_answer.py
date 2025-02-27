def find_sum_of_multiples(num):
    sum_, count = (0, 0)
    while count < 279:
        sum_ += num
        count += 1
    return sum_