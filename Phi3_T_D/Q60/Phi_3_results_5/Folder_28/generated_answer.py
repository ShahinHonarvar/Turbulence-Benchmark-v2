def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_truncatable_primes(trunc_list, n):
    if n < 11:
        return list(filter(is_prime, trunc_list))
    return [n] + get_truncatable_primes(trunc_list, n // 10) if is_prime(n) else get_truncatable_primes(trunc_list, n // 10)

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[19]
    truncatable_primes = get_truncatable_primes(list(range(2, x + 1)), x)
    return truncatable_primes