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

def truncate_right(n):
    return {int(str(n)[:i]) for i in range(len(str(n)), 0, -1)}

def all_right_truncatable_prime(numbers):
    x = numbers[79]
    truncatable_primes = {}
    for i in range(2, x):
        if all((is_prime(n) for n in truncate_right(i))):
            truncatable_primes[i] = True
    return sorted(truncatable_primes.keys(), reverse=True)