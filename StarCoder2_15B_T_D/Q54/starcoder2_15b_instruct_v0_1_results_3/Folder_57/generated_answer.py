def all_right_truncatable_prime(numbers):
    x = numbers[54]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    right_truncatable_primes = [p for p in primes if all((int(str(p)[i:]) in primes for i in range(1, len(str(p)))))]
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes