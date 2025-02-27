def composite_nums_between_indices(nums):

    def is_composite(num):
        if num < 2 or num % 2 == 0:
            return num > 2 if num % 2 == 0 else False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return True
        return False
    composite_set = set(filter(is_composite, nums))
    return composite_set