def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    check_number = numbers[630]
    primes = [prime for prime in range(2, check_number + 1) if is_prime(prime)]
    truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        for i in range(len(prime_str)):
            if not is_prime(int(prime_str[i:])):
                break
        else:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)