def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if 20 <= i <= 30 and num > 1 and any((num % j == 0 for j in range(2, num)))}