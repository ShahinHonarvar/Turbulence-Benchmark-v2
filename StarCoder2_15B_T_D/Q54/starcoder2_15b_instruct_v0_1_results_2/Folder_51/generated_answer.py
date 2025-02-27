def all_right_truncatable_prime(numbers):
    x = numbers[54]

    def is_right_truncatable_prime(n):
        if n < 10 and is_prime(n):
            return True
        elif n % 10 == 0:
            return False
        else:
            return is_prime(n) and is_right_truncatable_prime(n // 10)
    return sorted(filter(is_right_truncatable_prime, range(x)))