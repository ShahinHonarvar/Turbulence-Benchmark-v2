def all_left_right_truncatable_prime(numbers_tuple: tuple) -> list:
    x = numbers_tuple[758]
    left_right_truncatable_primes = set()
    for prime in range(2, x + 1):
        is_left_right_truncatable = True
        string_prime = str(prime)
        for i in range(len(string_prime)):
            left_truncatable = int(string_prime[i:])
            right_truncatable = int(string_prime[:len(string_prime) - i])
            if left_truncatable not in prime_set or right_truncatable not in prime_set:
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            left_right_truncatable_primes.add(prime)
    return sorted(left_right_truncatable_primes)