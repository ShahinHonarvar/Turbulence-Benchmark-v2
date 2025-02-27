def composite_nums_between_indices(nums):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    composite_nums = set()
    for i, num in enumerate(nums):
        if is_composite(num) and 23 <= i <= 23:
            composite_nums.add(num)
    return composite_nums