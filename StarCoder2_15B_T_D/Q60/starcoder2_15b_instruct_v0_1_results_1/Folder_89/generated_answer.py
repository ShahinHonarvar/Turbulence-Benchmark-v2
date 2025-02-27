def all_left_right_truncatable_prime(args):
    x = args[0]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable(num):
        if not is_prime(num):
            return False
        num_str = str(num)
        while len(num_str) > 1:
            num_str = num_str[1:]
            if not is_prime(int(num_str)):
                return False
        return True
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)