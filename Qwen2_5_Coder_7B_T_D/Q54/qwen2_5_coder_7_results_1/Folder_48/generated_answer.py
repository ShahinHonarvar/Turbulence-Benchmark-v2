def all_right_truncatable_prime(numbers):
    x = numbers[835]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generate_primes(limit):
        nonlocal primes
        for num in range(primes[-1] + 1, limit):
            if is_prime(num):
                primes.append(num)
    generate_primes(x)
    for prime in primes:
        str_prime = str(prime)
        is_right_truncatable = True
        for i in range(len(str_prime) - 1, 0, -1):
            if not is_prime(int(str_prime[:i])):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)