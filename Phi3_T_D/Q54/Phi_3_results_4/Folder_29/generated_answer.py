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

def right_truncatable_primes(n):
    right_trunc_primes = []
    for i in range(7, n, 2):
        num = i
        while num > 0:
            if not is_prime(num):
                break
            right_trunc_primes.append(num)
            num = num // 10
    return right_trunc_primes

def all_right_truncatable_prime(numbers):
    x = numbers[55]
    return sorted(right_truncatable_primes(x), reverse=True)