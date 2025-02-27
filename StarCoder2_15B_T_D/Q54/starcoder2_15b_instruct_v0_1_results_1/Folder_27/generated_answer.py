def all_right_truncatable_prime(input_tuple):
    x = input_tuple[79]

    def is_right_truncatable_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    right_truncatable_primes = [num for num in range(2, x) if is_right_truncatable_prime(num)]
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes