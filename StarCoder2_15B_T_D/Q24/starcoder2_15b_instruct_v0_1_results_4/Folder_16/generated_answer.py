def sum_of_divisors_in_range(num):
    result = 0
    for i in range(1, num + 1):
        if num % i == 0 and 228 <= i <= 846:
            result += i
    return result