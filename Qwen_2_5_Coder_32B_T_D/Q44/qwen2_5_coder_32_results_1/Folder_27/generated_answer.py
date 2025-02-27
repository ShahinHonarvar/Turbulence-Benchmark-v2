def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composite_numbers = set()
    for i in range(max(22, len(nums)), min(64, len(nums))):
        if is_composite(nums[i]):
            composite_numbers.add(nums[i])
    return composite_numbers