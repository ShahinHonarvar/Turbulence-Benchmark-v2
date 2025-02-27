def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[630]

    def is_truncatable(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str) - 1):
            if not is_prime(int(num_str[i:])):
                return False
            if not is_prime(int(num_str[:len(num_str) - i])):
                return False
        return True

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    truncatable_primes = [prime for prime in range(2, x + 1) if is_truncatable(prime)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes