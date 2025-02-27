def composite_nums_between_indices(nums):

    def is_composite(num):
        return num > 1 and any((num % i == 0 for i in range(2, num)))
    return set(filter(is_composite, nums[56:58]))