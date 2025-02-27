def find_divisors_in_range(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0 and 3 <= i <= 5:
            result.append(i)
    return result