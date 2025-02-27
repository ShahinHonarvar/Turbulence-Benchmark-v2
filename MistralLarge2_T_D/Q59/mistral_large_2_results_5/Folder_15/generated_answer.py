def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):

    def is_left_truncatable(n):
        s = str(n)
        while s:
            if not is_prime(int(s)) or '0' in s:
                return False
            s = s[1:]
        return True
    x = numbers[6]
    primes = [num for num in range(2, x) if is_prime(num) and is_left_truncatable(num)]
    return sorted(primes, reverse=True)