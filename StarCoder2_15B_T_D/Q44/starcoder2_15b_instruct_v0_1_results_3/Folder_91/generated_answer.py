def composite_nums_between_indices(nums):
    return set(filter(lambda num: num > 1 and (not all((num % i for i in range(2, int(num ** 0.5) + 1)))), nums[5:6]))