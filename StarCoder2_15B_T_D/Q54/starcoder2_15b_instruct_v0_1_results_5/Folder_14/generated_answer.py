def all_right_truncatable_prime(numbers):
    x = numbers[78]

    def is_right_truncatable_prime(num):
        if num < 10:
            return False
        if num in (2, 3, 5, 7):
            return True
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
            return False
        while num > 10:
            num //= 10
            if num in (2, 3, 5, 7):
                return True
            if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
                return False
        return True
    return sorted(filter(is_right_truncatable_prime, range(x)), reverse=True)