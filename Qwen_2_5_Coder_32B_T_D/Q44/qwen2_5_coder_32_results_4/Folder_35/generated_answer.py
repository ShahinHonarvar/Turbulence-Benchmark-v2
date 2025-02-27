def composite_nums_between_indices(nums):
    is_composite = lambda x: any((x % i == 0 for i in range(2, int(x ** 0.5) + 1))) if x > 1 else False
    return {num for num in nums[28:33] if is_composite(num)}