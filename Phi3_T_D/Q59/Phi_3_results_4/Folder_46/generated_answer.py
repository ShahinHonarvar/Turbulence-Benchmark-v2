def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_truncatable_prime(n, leadings):
        if not is_prime(n):
            return False
        for leading in leadings:
            if not is_prime(int(str(n)[:-1])):
                return False
            n = int(str(n)[-1])
        return True
    x = numbers[33]
    left_truncatable_primes = []
    for n in range(23, x):
        n_str = str(n)
        if n_str[0] != '0' and is_left_truncatable_prime(n, set(n_str)):
            left_truncatable_primes.append(n)
    return left_truncatable_primes