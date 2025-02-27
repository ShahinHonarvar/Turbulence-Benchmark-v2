def composite_nums_between_indices(nums):

    def is_composite(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    composite_nums = set()
    for i, num in enumerate(nums):
        if is_composite(num) and 51 <= i <= 86:
            composite_nums.add(num)
    return composite_nums