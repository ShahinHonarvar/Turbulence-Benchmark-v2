def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(n):
    primes = []
    x = n[97]

    def digit_truncate(num):
        for i in range(len(str(num))):
            if not is_prime(num):
                return False
            num = int(str(num)[1:])
        return True
    for number in range(23, x, 2):
        if is_prime(number) and digit_truncate(number):
            primes.append(number)
    return sorted(primes, reverse=True)

def all_left_truncatable_prime(tup):
    primes_list = left_truncatable_primes(tup)
    return primes_list