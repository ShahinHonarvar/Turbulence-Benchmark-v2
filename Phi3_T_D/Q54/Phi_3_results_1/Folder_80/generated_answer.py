def all_right_truncatable_prime(numbers):
    n = numbers[14]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        return all((is_prime(num // 10 ** i) for i in range(len(str(num)))))
    return sorted([num for num in range(n, 1, -1) if is_prime(num) and is_right_truncatable_prime(num)], reverse=True)