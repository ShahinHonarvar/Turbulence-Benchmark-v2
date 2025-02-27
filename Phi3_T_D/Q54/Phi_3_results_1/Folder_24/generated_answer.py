def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

def right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[65]
    primes = [num for num in range(2, x) if right_truncatable_prime(num)]
    return sorted(list(set(primes)), reverse=True)