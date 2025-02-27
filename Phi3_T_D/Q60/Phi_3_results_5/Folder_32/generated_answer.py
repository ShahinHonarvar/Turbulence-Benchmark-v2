def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    max_check = numbers[42]
    truncatable_primes = []
    for prime in range(11, max_check + 1):
        num_str = str(prime)
        if not prime % 10 in (0, 2, 4, 5, 6, 8):
            if all((is_prime(int(num_str[i:])) and is_prime(int(num_str[:max_check - len(num_str) + i + 1])) for i in range(len(num_str)))):
                truncatable_primes.append(prime)
    return sorted(truncatable_primes)