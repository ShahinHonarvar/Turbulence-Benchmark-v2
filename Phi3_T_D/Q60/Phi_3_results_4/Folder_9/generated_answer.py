def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(primes):

    def truncatable(n, primes):
        str_n = str(n)
        if len(str_n) == 1:
            return True
        if not is_prime(n):
            return False
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or int(str_n[i:]) not in primes:
                return False
            if not is_prime(int(str_n[:i])) or int(str_n[:i]) not in primes:
                return False
        return True
    primes_set = set(primes)
    return [n for n in range(11, n + 1) if truncatable(n, primes_set)]

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    primes = set([2, 3, 5, 7])
    num = 11
    while num <= x:
        if is_prime(num):
            primes.add(num)
        num += 2
    return is_truncatable(primes)