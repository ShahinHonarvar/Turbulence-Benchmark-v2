def composite_nums_between_indices(nums):
    composite_set = set()
    for num in nums[56:83]:
        if num > 1:
            factors = [i for i in range(2, int(num ** 0.5) + 1) if num % i == 0]
            if factors:
                composite_set.add(num)
    return composite_set