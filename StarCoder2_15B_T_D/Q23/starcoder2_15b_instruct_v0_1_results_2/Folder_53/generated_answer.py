def find_divisors_in_range(num):
    divisors = []
    for i in range(2, num + 1):
        if num % i == 0 and 4 <= i <= 9:
            divisors.append(i)
    return divisors