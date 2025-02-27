def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def left_and_right_check(n):
    str_n, result = (str(n), True)
    for i in range(len(str_n) - 1):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i - 1])):
            result = False
            break
    return result

def all_left_right_truncatable_prime(numbers):
    x = numbers[33]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    result = [p for p in primes if left_and_right_check(p)]
    return sorted(result)