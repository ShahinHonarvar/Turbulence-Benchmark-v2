def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_truncatable_primes(n):

    def recursive_helper(prefix, suffix):
        if len(prefix) > 1 and is_prime(int(prefix)):
            truncatable_primes.add(int(prefix))
        if len(suffix) > 1 and is_prime(int(suffix)):
            truncatable_primes.add(int(suffix))
        if len(prefix) > 0 and len(suffix) > 0:
            recursive_helper(prefix[:-1], suffix[1:])
    truncatable_primes = set()
    recursive_helper(str(n), str(n))
    return sorted(list(truncatable_primes))