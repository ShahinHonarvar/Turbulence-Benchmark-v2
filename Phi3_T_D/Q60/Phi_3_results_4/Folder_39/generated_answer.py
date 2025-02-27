def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable_prime(n):
    if not str(n).startswith('0') and is_prime(n):
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[0:i + 1])):
                return False
        return True
    return False

def all_left_right_truncatable_primes(range_tuple):
    x = range_tuple[30]
    primes = []
    for number in range(2, x + 1):
        if is_left_and_right_truncatable_prime(number):
            primes.append(number)
    return sorted(primes, reverse=True)