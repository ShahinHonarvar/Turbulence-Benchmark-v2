def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(prime, primes_set):
        str_prime = str(prime)
        for i in range(len(str_prime)):
            if not is_prime(int(str_prime[i:])) or (str_prime[i:] != str_prime and (not is_prime(int(str_prime[:i + 1])))):
                return False
        return True
    x = numbers[77]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    primes_set = set(primes)
    return [p for p in primes if is_truncatable_prime(p, primes_set)]