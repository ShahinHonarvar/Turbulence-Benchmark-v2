def all_right_truncatable_prime(numbers):
    x = numbers[73]

    def is_right_truncatable_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        while number >= 10:
            number //= 10
            if number < 2:
                return False
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    return False
        return True
    right_truncatable_primes = [number for number in range(x) if is_right_truncatable_prime(number)]
    return sorted(right_truncatable_primes, reverse=True)