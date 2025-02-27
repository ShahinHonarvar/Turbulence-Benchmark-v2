def all_left_right_truncatable_prime(numbers):
    x = numbers[6]
    primes = [2, 3, 5, 7]
    result = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(11, x + 1):
        s = str(num)
        if '0' in s:
            continue
        if all((is_prime(int(s[:i])) for i in range(1, len(s)))) and all((is_prime(int(s[-i:])) for i in range(1, len(s)))):
            primes.append(num)
    for p in sorted(primes, reverse=True):
        if all((is_prime(int(p[:i])) for i in range(1, len(p)))) and all((is_prime(int(p[-i:])) for i in range(1, len(p)))):
            result.append(p)
    return result