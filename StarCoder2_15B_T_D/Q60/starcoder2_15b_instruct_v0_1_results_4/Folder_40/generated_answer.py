def all_left_right_truncatable_prime(x):
    x = x[10]
    left_truncatable_primes = [2, 3, 5, 7]
    for i in range(1, x + 1):
        for prime in left_truncatable_primes:
            if not is_left_truncatable_prime(prime, i):
                break
        else:
            left_truncatable_primes.append(i)
    right_truncatable_primes = [2, 3, 5, 7]
    for i in range(1, x + 1):
        for prime in right_truncatable_primes:
            if not is_right_truncatable_prime(prime, i):
                break
        else:
            right_truncatable_primes.append(i)
    return sorted(left_truncatable_primes + right_truncatable_primes, reverse=True)

def is_left_truncatable_prime(prime, i):
    if i < 10:
        return str(prime).startswith(str(i))
    else:
        return is_left_truncatable_prime(prime // 10, i // 10) and is_prime(prime % 10)

def is_right_truncatable_prime(prime, i):
    if i < 10:
        return str(prime).endswith(str(i))
    else:
        return is_right_truncatable_prime(prime % 10, i % 10) and is_prime(prime // 10)

def is_prime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True