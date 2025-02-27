from sympy import isprime

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[630]
    right_truncatable_primes = []

    def primes_with_rightmost_digit(last_digit):
        return set((p for p in range(10 * last_digit, last_digit * 10, 10) if isprime(p)))
    for last_digit in range(1, 10):
        primes = primes_with_rightmost_digit(last_digit)
        candidate_set = set()
        for prime in primes:
            remaining_digits = prime // 10
            while remaining_digits > 0:
                if remaining_digits not in primes_with_rightmost_digit(remaining_digits % 10):
                    break
                remaining_digits //= 10
            else:
                candidate_set.add(prime)
        right_truncatable_primes.extend(sorted(candidate_set))
    return sorted(right_truncatable_primes, reverse=True)