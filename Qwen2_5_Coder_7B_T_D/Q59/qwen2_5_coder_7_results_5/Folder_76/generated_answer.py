def all_left_truncatable_prime(numbers):
    x = numbers[370]
    primes = set()

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((is_prime(int(str_num[:i])) for i in range(1, len(str_num) + 1))):
            primes.add(num)
    return sorted(primes, reverse=True)