def find_sum_of_multiples(num):
    count, sum = (0, 0)
    i = 1
    while count < 445:
        if i % num == 0:
            sum += i
            count += 1
        i += 1
    return sum