def all_left_truncatable_prime(numbers):
    x = numbers[33]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    for num in range(11, x, 2):
        if str(num)[0] in '024568' or not is_prime(num):
            continue
        if is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)