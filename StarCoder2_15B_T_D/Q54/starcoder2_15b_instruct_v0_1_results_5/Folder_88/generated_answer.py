def all_right_truncatable_prime(numbers):
    x = numbers[93]

    def is_right_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        return is_prime(num) and is_right_truncatable_prime(int(str(num)[:-1]))
    return sorted([i for i in range(x) if is_right_truncatable_prime(i)])