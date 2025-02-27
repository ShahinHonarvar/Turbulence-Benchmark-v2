def composite_nums_between_indices(nums):
    composite_nums = [num for num in nums if num > 1 and (not all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))))]
    return set(composite_nums[68:87])