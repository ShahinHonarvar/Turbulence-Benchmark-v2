def composite_nums_between_indices(nums):
    return {n for i, n in enumerate(nums) if 22 <= i <= 88 and is_composite(n)}

def is_composite(n):
    return n > 1 and any((n % i == 0 for i in range(2, n)))