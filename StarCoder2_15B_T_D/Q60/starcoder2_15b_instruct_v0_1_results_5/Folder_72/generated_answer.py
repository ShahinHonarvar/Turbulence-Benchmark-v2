def all_left_right_truncatable_prime(tuple_of_positive_integers):

    def is_truncatable_prime(num):
        num_str = str(num)
        for i in range(len(num_str) - 1):
            if not (is_prime(int(num_str[i:])) and is_prime(int(num_str[:len(num_str) - i]))):
                return False
        return True

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = tuple_of_positive_integers[31]
    truncatable_primes = [prime for prime in range(2, x + 1) if is_truncatable_prime(prime)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes