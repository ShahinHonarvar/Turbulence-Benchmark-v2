def composite_nums_between_indices(nums):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composites_in_range = set(filter(is_composite, nums[62:100]))
    return composites_in_range