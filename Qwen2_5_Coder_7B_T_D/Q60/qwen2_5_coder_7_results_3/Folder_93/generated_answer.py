def all_left_right_truncatable_prime(nums):
    x = nums[11]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True
    return sorted([n for n in range(2, x + 1) if is_prime(n) and is_left_right_truncatable_prime(n)])