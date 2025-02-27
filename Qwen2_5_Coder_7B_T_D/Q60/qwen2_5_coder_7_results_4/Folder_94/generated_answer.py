import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[43]
    primes = [2, 3, 5, 7]
    result = []
    for num in range(11, x + 1, 2):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((is_prime(int(str_num[:i])) and is_prime(int(str_num[i:])) for i in range(1, len(str_num)))):
            primes.append(num)
    for prime in primes:
        if prime >= 10 and all((is_prime(int(str(prime)[:i])) and is_prime(int(str(prime)[i:])) for i in range(1, len(str(prime))))):
            result.append(prime)
    return sorted(result)