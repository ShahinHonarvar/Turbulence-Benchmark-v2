def all_left_truncatable_prime(nums):
    x = nums[96]

    def is_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        if num % 10 == 0:
            return False
        return is_prime(num) and is_truncatable_prime(num // 10)

    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return sorted(filter(is_truncatable_prime, range(x)), reverse=True)