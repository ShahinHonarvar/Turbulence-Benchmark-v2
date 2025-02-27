def composite_nums_between_indices(nums):
    return set((num for i, num in enumerate(nums) if 52 <= i <= 71 and is_composite(num)))

def is_composite(num):
    return any((num % i == 0 for i in range(2, num)))