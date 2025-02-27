def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[86]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(num):
        num_str = str(num)
        for i in range(len(num_str)):
            truncated_num = int(num_str[i:])
            if not is_prime(truncated_num):
                return False
            truncated_num = int(num_str[:len(num_str) - i])
            if not is_prime(truncated_num):
                return False
        return True
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)