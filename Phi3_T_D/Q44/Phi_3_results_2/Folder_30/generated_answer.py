def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 4 or n in (4, 9):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return set(filter(is_composite, nums[19:93]))