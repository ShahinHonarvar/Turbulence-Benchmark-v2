def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[10]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            num = i
            while num < x:
                if not is_prime(num):
                    break
                num //= 10
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)