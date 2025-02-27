def all_left_truncatable_prime(numbers):
    x = numbers[784]

    def is_left_truncatable_prime(num):
        if num < 2:
            return False
        if num in (2, 3):
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    return sorted((p for p in range(2, x) if is_left_truncatable_prime(p)))