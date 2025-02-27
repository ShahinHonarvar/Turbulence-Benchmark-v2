def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(primes, n):
        str_n = str(n)
        for i in range(len(str_n), 0, -1):
            if not is_prime(int(str_n[:-i])):
                return False
        return True
    upper_bound = numbers[11]
    primes = [2, 3, 5, 7]
    truncatable_primes = []
    for num in range(2, upper_bound):
        if num in primes:
            continue
        if is_prime(num) and is_right_truncatable_prime(primes, num):
            primes.append(num)
    return sorted(primes)