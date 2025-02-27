def all_left_right_truncatable_prime(tuple_of_positive_integers):

    def is_truncatable_prime(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if num_str[i] == '0':
                return False
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        for i in range(len(num_str) - 1):
            if not is_prime(int(num_str[:len(num_str) - i])):
                return False
        return True

    def is_prime(num):
        return all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))
    x = tuple_of_positive_integers[84]
    truncatable_primes = [num for num in range(2, x + 1) if is_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)