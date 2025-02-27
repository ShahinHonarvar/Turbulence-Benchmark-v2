def all_left_truncatable_prime(numbers):
    primes_below_x = set()
    for num in range(2, numbers[14]):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes_below_x.add(num)

    def is_left_truncatable(prime, primes_set):
        str_prime = str(prime)
        while str_prime:
            if int(str_prime) not in primes_set or '0' in str_prime:
                return False
            str_prime = str_prime[1:]
        return True
    left_truncatable_primes = [prime for prime in primes_below_x if is_left_truncatable(prime, primes_below_x)]
    return sorted(left_truncatable_primes, reverse=True)