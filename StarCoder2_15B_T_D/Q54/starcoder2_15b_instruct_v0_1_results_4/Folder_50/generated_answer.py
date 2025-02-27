def all_right_truncatable_prime(numbers):

    def right_truncatable_prime_helper(num):
        if num < 10 and is_prime(num):
            return [num]
        elif num % 10 == 0:
            return []
        elif is_prime(num):
            return [num] + right_truncatable_prime_helper(num // 10)
        else:
            return []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = numbers[57]
    return sorted(right_truncatable_prime_helper(x), reverse=True)