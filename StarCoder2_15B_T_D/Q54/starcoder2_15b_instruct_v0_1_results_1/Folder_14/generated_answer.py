def all_right_truncatable_prime(input_tuple):
    x = input_tuple[78]

    def is_right_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        else:
            return is_prime(num) and is_right_truncatable_prime(int(str(num)[:-1]))

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    right_truncatable_primes = [num for num in range(1, x) if is_right_truncatable_prime(num)]
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes