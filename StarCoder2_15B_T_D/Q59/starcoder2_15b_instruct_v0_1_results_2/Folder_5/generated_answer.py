def all_left_truncatable_prime(x):

    def is_left_truncatable_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    left_truncatable_primes = []
    for i in range(1, x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return left_truncatable_primes