def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[70]

    def is_left_right_truncatable_prime(num):
        num_str = str(num)
        if not is_prime(num):
            return False
        for i in range(len(num_str) - 1):
            if not is_prime(int(num_str[i + 1:])) or not is_prime(int(num_str[:len(num_str) - i - 1])):
                return False
        return True

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_truncatable_primes(num):
        if is_left_right_truncatable_prime(num):
            return [num]
        return []
    truncatable_primes = []
    for i in range(2, x + 1):
        truncatable_primes += get_truncatable_primes(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes