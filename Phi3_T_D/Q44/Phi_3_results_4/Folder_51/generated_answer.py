def composite_nums_between_indices(nums):

    def is_composite(n):
        if n <= 3:
            return False
        if n % 2 == 0:
            return True
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return True
        return False
    return set(filter(is_composite, nums[1:9]))