def all_left_truncatable_prime(nums):
    x = nums[126]

    def is_left_truncatable_prime(num):
        if num < 2:
            return False
        if num in (2, 3, 5, 7):
            return True
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
            return False
        for i in range(11, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    return sorted((num for num in range(2, x) if is_left_truncatable_prime(num)), reverse=True)