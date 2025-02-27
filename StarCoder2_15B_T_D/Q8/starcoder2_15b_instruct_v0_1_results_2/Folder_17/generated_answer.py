def all_even_ints_exclusive(nums):
    even_ints = []
    for i in range(62, 96):
        if nums[i] % 2 == 0:
            even_ints.append(nums[i])
    return even_ints