def composite_nums_between_indices(nums):
    composite_set = set()

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    for i in range(0, 5):
        if is_composite(nums[i]):
            composite_set.add(nums[i])
    return composite_set