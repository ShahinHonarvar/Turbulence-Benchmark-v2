def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 2:
            return False
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0:
                return True
        return False
    return {num for num in nums[262:747] if is_composite(num)}