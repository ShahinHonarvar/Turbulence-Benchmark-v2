def all_left_truncatable_prime(p):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [i for i in range(2, p[100]) if is_prime(i)]

    def is_left_truncatable(prime):
        if prime <= 10:
            return True
        return all((is_prime(int(str(prime)[i:])) for i in range(len(str(prime)))))
    return sorted(filter(is_left_truncatable, primes))