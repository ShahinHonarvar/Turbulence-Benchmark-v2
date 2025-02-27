def is_composite(num):
    return all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))

def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if is_composite(num) and 22 <= i <= 50}