def composite_nums_between_indices(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_composite(n):
        return not is_prime(n) and n != 1
    return {nums[i] for i in range(62, 64) if is_composite(nums[i])}