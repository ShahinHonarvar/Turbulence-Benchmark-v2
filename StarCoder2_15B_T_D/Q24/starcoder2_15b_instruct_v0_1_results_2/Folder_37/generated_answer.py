def sum_of_divisors_in_range(num):
    result = 0
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 7 == 0:
            result += i
    return result