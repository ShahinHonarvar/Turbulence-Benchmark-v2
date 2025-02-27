def all_left_truncatable_prime(nums):
    x = nums[85]

    def is_left_truncatable_prime(num):
        if num < 10 and is_prime(num):
            return True
        elif num >= 10:
            if num % 10 == 0:
                return False
            else:
                return is_prime(num) and is_left_truncatable_prime(num // 10)
        else:
            return False

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return sorted([num for num in range(x) if is_left_truncatable_prime(num)])