def all_left_truncatable_prime(primes_tuple):

    def is_left_truncatable(num, prime_list):
        while num > 0:
            if num not in prime_list:
                return False
            num = num % 10 ** len(str(num))
        return True
    x = primes_tuple[433]
    truncated_primes = [str(p) for p in primes_tuple if is_left_truncatable(p, primes_tuple) and p < x]
    truncated_primes.sort(reverse=True)
    return [int(tp) for tp in truncated_primes]