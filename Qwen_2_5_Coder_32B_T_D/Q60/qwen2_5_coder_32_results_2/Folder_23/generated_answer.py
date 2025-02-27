def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    primes = set()

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x + 1):
        s = str(num)
        if '0' not in s:
            lr_truncatable = True
            for i in range(1, len(s) - 1):
                if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                    lr_truncatable = False
                    break
            if lr_truncatable and is_prime(num):
                primes.add(num)
    return sorted(primes, reverse=True)