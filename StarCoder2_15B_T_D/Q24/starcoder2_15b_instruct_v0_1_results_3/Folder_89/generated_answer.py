def sum_of_divisors_in_range(number):
    result = 0
    for i in range(1, number + 1):
        if number % i == 0 and 14 <= i <= 48:
            result += i
    return result