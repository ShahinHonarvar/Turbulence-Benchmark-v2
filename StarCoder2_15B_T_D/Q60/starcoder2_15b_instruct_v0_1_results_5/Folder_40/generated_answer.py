def all_left_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[10]
    left_truncatable_primes = []
    right_truncatable_primes = []
    for number in range(2, x + 1):
        if all((number % divisor != 0 for divisor in range(2, int(number ** 0.5) + 1))):
            left_truncatable_primes.append(number)
            right_truncatable_primes.append(number)
    left_truncatable_primes = [prime for prime in left_truncatable_primes if not str(prime).startswith('0')]
    right_truncatable_primes = [prime for prime in right_truncatable_primes if not str(prime).endswith('0')]
    for i in range(1, len(str(x))):
        left_truncatable_primes = [prime for prime in left_truncatable_primes if prime // 10 in left_truncatable_primes]
        right_truncatable_primes = [prime for prime in right_truncatable_primes if prime % 10 in right_truncatable_primes]
    left_right_truncatable_primes = [prime for prime in left_truncatable_primes if prime in right_truncatable_primes]
    return sorted(left_right_truncatable_primes, reverse=True)