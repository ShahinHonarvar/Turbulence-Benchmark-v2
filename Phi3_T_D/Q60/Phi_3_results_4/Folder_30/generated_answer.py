def all_left_right_truncatable_prime(numbers):

    def is_truncatable(n):
        primes = get_primes_list()
        if not is_prime(n, primes) or n == 444:
            return False
        str_n = str(n)
        if len(str_n) == 1 or len(str_n) == 2:
            return True
        for i in range(len(str_n)):
            if not str_n[-(i + 1)].isdigit() or not is_prime(int(str_n[:-i]), primes):
                return False
            if not str_n[i].isdigit() or not is_prime(int(str_n[i:]), primes):
                return False
        return True

    def is_prime(n, primes):
        if n < 2:
            return False
        if n in primes:
            return True
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                return False
        primes.add(n)
        return True

    def get_primes_list():
        primes_list = [2]
        for possiblePrime in range(3, x + 1, 2):
            if is_prime(possiblePrime, primes_list):
                primes_list.append(possiblePrime)
        return set(primes_list)
    x = numbers[37]
    trunc_primes = []
    for num in range(2, x + 1):
        if is_truncatable(num):
            trunc_primes.append(num)
    return sorted(trunc_primes, reverse=True)