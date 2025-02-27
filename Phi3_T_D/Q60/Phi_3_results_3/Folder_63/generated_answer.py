def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(primes_set, number):
    str_num = str(number)
    for i in range(1, len(str_num)):
        if int(str_num[i:]) not in primes_set or int(str_num[:i]) not in primes_set:
            return False
    return True

def all_left_right_truncatable_prime(numbers_tuple):
    upper_limit = numbers_tuple[88]
    primes_set = {i for i in range(2, upper_limit + 1) if is_prime(i)}
    truncatable_primes = []
    for prime in primes_set:
        if is_truncatable(primes_set, prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)