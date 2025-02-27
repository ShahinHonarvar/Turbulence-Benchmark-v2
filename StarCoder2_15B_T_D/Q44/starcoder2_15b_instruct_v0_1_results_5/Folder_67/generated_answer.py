def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if i >= 56 and i <= 82 and (num not in {2, 3, 5, 7, 11, 13, 17, 19})}