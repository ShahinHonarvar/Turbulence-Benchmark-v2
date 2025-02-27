def all_left_right_truncatable_prime(nums):
    x = nums[30]

    def is_truncatable_prime(num):
        if num < 10:
            return False
        if num in [2, 3, 5, 7]:
            return True
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
            return False
        while num > 10:
            num = int(str(num)[1:])
            if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
                return False
        return True
    return sorted(filter(is_truncatable_prime, range(2, x + 1)), reverse=True)