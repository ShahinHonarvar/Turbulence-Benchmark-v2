def all_left_truncatable_prime(numbers):
    x = numbers[11]
    primes = [2, 3, 5, 7]
    result = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(11, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        if all((is_prime(int(num_str[:i + 1])) for i in range(len(num_str)))):
            primes.append(num)
    primes.sort()
    for prime in primes:
        if all((is_prime(int(prime[:i + 1])) for i in range(len(prime)))):
            result.append(prime)
    return result