def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[126]
    left_truncatable_primes = []
    for num in range(2, x):
        s = str(num)
        if '0' not in s and all((is_prime(int(s[i:])) for i in range(len(s)))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)