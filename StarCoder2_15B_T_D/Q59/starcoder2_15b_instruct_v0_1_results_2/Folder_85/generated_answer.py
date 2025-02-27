def all_left_truncatable_prime(tup):
    x = tup[94]
    left_truncatable_primes = []
    for i in range(2, x):
        is_left_truncatable = True
        num = i
        while num > 0:
            if num % 10 == 0 or not is_prime(num):
                is_left_truncatable = False
                break
            num //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True