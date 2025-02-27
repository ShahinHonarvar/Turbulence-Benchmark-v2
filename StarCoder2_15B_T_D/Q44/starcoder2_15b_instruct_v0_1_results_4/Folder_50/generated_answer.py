def composite_nums_between_indices(nums):
    is_composite = lambda num: any((num % i == 0 for i in range(2, int(num ** 0.5) + 1)))
    return {num for i, num in enumerate(nums) if 56 <= i <= 57 and is_composite(num)}