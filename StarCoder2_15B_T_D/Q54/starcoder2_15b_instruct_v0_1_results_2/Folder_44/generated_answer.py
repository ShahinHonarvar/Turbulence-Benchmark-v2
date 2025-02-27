def all_right_truncatable_prime(nums):
    x = nums[39]

    def is_right_truncatable_prime(num):
        if num < 10:
            return False
        if num in [2, 3, 5, 7]:
            return True
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
            return False
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True

    def is_prime(num):
        if num < 2:
            return False
        if num in [2, 3]:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        for i in range(5, int(num ** 0.5) + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                return False
        return True
    return sorted((num for num in range(2, x) if is_right_truncatable_prime(num)))