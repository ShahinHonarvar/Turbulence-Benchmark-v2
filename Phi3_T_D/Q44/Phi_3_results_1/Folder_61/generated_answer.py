def composite_nums_between_indices(nums):
    composites = {num for num in nums[:8] if any((num % i == 0 for i in range(2, int(num ** 0.5) + 1))) and num != 1}
    return composites