def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                break
            n = n // 10
        return n == 0
    x = nums[26]
    res_list = [i for i in range(2, x) if is_prime(i) and is_right_truncatable(i)]
    return sorted(res_list)