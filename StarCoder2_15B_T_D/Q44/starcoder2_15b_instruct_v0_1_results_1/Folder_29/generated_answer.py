def composite_nums_between_indices(nums):

    def is_composite(num):
        return num > 1 and any((num % i == 0 for i in range(2, int(num ** 0.5) + 1)))
    composite_nums = set(filter(is_composite, nums))
    return set((num for num in composite_nums if 52 <= nums.index(num) <= 71))