def all_left_truncatable_prime(nums):
    x = nums[20]

    def is_truncatable_prime(num):
        if num < 2 or any((digit == 0 for digit in str(num))):
            return False
        for i in range(1, len(str(num))):
            if not is_prime(int(str(num)[i:])):
                return False
        return is_prime(num)

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return sorted([num for num in range(2, x) if is_truncatable_prime(num)], reverse=True)