def composite_nums_between_indices(nums):
    assert all((isinstance(num, int) and num > 0 for num in nums)), 'Input must be a list of positive integers'
    composite_nums = set()
    for num in nums[22:51]:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                composite_nums.add(num)
                break
    return composite_nums