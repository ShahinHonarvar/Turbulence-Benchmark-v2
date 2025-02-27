def all_even_ints_exclusive(nums):
    even_nums = []
    for i in range(len(nums)):
        if i >= 22 and i < 24 and (nums[i] % 2 == 0):
            even_nums.append(nums[i])
    return even_nums