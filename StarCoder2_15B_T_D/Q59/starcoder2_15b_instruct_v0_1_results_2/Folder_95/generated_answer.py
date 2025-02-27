def all_left_truncatable_prime(input_tuple):
    x = input_tuple[0]

    def is_prime(num):
        if num == 2:
            return True
        if num % 2 == 0 or num <= 1:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if not is_prime(num):
            return False
        while num >= 10:
            num //= 10
            if not is_prime(num):
                return False
        return True
    return sorted((num for num in range(2, x) if is_left_truncatable_prime(num)))