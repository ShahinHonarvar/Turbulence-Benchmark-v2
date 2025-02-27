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

def all_right_truncatable_prime(numbers):
    x = numbers[24]
    right_truncatable_primes = [i for i in range(7, x) if is_prime(i) and set(str(i)[i:]) <= {'2', '3', '5', '7'}]
    return sorted(right_truncatable_primes)