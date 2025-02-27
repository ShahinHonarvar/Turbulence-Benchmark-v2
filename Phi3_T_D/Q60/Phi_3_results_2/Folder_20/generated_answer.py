def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        n_str = str(n)
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:i + 1])):
                return False
        return True

    def get_all_truncatable_primes(limit):
        truncatable_primes = []
        for num in range(11, limit + 1):
            if is_left_right_truncatable_prime(num):
                truncatable_primes.append(num)
        return truncatable_primes
    x = numbers[100]
    return get_all_truncatable_primes(x)