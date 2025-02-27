def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start_idx, end_idx = (28, 40)
    composites = {num for num in nums[start_idx:end_idx + 1] if is_composite(num)}
    return composites