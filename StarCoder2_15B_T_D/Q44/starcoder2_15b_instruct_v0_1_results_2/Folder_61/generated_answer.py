def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums:
        is_composite = False
        for i in range(2, num):
            if num % i == 0:
                is_composite = True
                break
        if is_composite and 0 <= nums.index(num) <= 7:
            composite_nums.add(num)
    return composite_nums