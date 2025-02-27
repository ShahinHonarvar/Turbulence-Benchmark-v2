def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 2:
            return False
        for f in range(2, int(n ** 0.5) + 1):
            if n % f == 0:
                return True
        return False
    return {n for i, n in enumerate(nums[25:88], start=25) if is_composite(n)}