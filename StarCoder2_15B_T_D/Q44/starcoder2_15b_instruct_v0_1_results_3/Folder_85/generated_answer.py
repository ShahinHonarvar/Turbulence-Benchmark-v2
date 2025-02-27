def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if 3 <= i <= 5 and is_composite(num)}

def is_composite(num):
    return num > 1 and any((num % i == 0 for i in range(2, num)))