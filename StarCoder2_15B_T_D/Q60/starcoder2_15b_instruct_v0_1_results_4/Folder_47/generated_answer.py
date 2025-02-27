def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[49]

    def is_truncatable(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        for i in range(len(num_str) - 1, -1, -1):
            if not is_prime(int(num_str[:i + 1])):
                return False
        return True

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)