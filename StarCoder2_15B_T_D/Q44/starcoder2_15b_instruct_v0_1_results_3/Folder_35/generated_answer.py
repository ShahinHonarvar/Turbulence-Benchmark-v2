def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composite_nums = set()
    for i, num in enumerate(nums):
        if is_composite(num) and 28 <= i <= 32:
            composite_nums.add(num)
    return composite_nums