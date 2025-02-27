def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(number):
        if number < 10:
            return is_prime(number)
        if number % 10 == 0:
            return False
        return is_truncatable_prime(number // 10) and is_prime(number)

    def is_prime(number):
        if number < 2:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True
    x = numbers[61]
    return sorted((number for number in range(1, x + 1) if is_truncatable_prime(number)))