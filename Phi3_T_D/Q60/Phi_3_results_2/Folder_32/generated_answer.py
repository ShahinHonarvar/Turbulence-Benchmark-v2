def all_left_right_truncatable_prime(nums):
    x = nums[42]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate(n):
        str_n = str(n)
        return [int(str_n[i:]) for i in range(len(str_n))]

    def truncatable(n):
        if not is_prime(n):
            return False
        for tail in truncate(n):
            if not is_prime(tail):
                return False
        return True
    return sorted([n for n in range(2, x + 1) if truncatable(n)])