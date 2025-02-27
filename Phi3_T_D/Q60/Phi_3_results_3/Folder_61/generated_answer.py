def all_left_right_truncatable_prime(numbers, x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for end in range(1, len(str_n)):
            if not is_prime(int(str_n[end:])) or not is_prime(int(str_n[:end])):
                return False
        if len(str_n) > 1:
            return False
        return True
    primes = [2, 3, 5, 7]
    for number in range(11, x + 1):
        if is_prime(number) and is_truncatable_prime(number):
            primes.append(number)
    return sorted(primes, reverse=True)