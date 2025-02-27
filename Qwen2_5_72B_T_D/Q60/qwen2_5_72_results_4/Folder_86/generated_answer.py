def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    length = len(str(n))
    for i in range(1, length):
        trunc = int(str(n)[i:-i] if i < length - i else str(n)[i:])
        if not is_prime(trunc):
            return False
    return is_prime(n)

def all_left_right_truncatable_prime(numbers):
    x = numbers[126]
    primes = [i for i in range(2, x + 1) if is_truncatable_prime(i)]
    return sorted(primes, reverse=True)