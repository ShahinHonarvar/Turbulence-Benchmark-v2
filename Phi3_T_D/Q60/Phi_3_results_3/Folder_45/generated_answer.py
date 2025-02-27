def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_and_right_truncatable_prime(number):
        string_number = str(number)
        for i in range(1, len(string_number) - 1):
            if not is_prime(int(string_number[i:])) or not is_prime(int(string_number[:-i])):
                return False
        return is_prime(number)
    x = numbers[61]
    return sorted([i for i in range(2, x + 1) if is_left_and_right_truncatable_prime(i)])