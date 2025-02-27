def all_left_right_truncatable_prime(primes_tuple):
    end_prime = primes_tuple[630]
    truncatable_primes = [p for p in primes_tuple if 10 <= p <= end_prime]
    left_truncatable = set((p for p in truncatable_primes if all((int(p[i:]) in truncatable_primes for i in range(1, len(str(p)))))))
    right_truncatable = set((p for p in truncatable_primes if all((int(p[:i + 1]) in truncatable_primes for i, c in enumerate(str(p)) if c is not '0'))))
    result = sorted(left_truncatable.intersection(right_truncatable), reverse=True)
    return result