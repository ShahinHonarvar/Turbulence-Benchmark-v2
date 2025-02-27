def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[222:223]:
        if num > 1 and (not all((num % d != 0 for d in range(2, int(num ** 0.5) + 1)))):
            composites.add(num)
    return composites