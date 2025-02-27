def all_left_truncatable_prime(nums):

    def is_left_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        return is_prime(num) and is_left_truncatable_prime(int(str(num)[1:]))

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = nums[92]
    return sorted(filter(is_left_truncatable_prime, range(x)))