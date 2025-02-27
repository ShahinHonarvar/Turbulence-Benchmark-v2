def composite_nums_between_indices(nums):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    range_start, range_end = (527, 538)
    return {n for n in nums[range_start:range_end + 1] if is_composite(n)}