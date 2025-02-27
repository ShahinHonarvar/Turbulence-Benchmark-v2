def all_right_truncatable_prime(numbers):
    x = numbers[792]

    def is_right_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        return is_prime(num) and is_right_truncatable_prime(int(str(num)[:-1]))
    truncatable_primes = [num for num in range(1, x) if is_right_truncatable_prime(num)]
    return sorted(truncatable_primes)