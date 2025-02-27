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

def all_left_truncatable_prime(numbers):
    x = numbers[30]
    left_truncatable_primes = []
    for prime_candidate in range(x - 1, 1, -1):
        if not is_prime(prime_candidate):
            continue
        number_str = str(prime_candidate)
        if '0' in number_str:
            continue
        is_left_truncatable = True
        for i in range(len(number_str)):
            if not is_prime(int(number_str[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(prime_candidate)
    return left_truncatable_primes