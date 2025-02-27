def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums[0:8]:
        for i in range(2, num):
            if num % i == 0:
                composite_nums.add(num)
                break
    return composite_nums