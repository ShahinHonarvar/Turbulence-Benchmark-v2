def all_right_truncatable_prime(numbers):
    x = numbers[39]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        if not is_prime(num):
            return False
        temp = num
        while temp:
            temp = temp // 10
            if not is_prime(num % (10 ** len(str(num)) // 10)):
                return False
        return True
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])