def all_left_truncatable_prime(tuple_of_integers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, prime_set):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = tuple_of_integers[31]
    prime_set = set()
    left_truncatable_primes = []
    for num in reversed(range(2, x)):
        if num not in prime_set and is_left_truncatable(num, prime_set):
            prime_set.add(num)
            left_truncatable_primes.append(num)
    return left_truncatable_primes