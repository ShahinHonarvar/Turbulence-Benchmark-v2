def all_left_truncatable_prime(numbers):
    x = numbers[126]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(8, x):
        str_num = str(num)
        if '0' not in str_num:
            if all((is_prime(int(str_num[:i])) for i in range(1, len(str_num) + 1))):
                primes.append(num)
    left_truncatable_primes = [p for p in primes if all((is_prime(int(str(p)[:i])) for i in range(1, len(str(p)) + 1)))]
    return sorted(left_truncatable_primes, reverse=True)