def sum_of_divisors_in_range(num):
    result = 0
    for i in range(1, num + 1):
        if num % i == 0 and 43 <= i <= 46:
            result += i
    return result