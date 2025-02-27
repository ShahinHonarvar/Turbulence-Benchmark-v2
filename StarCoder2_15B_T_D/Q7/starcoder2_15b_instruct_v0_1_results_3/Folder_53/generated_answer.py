def all_even_ints_inclusive(nums):
    even_ints = []
    for i in range(len(nums)):
        if i >= 100 and i <= 200 and (nums[i] % 2 == 0):
            even_ints.append(nums[i])
    return even_ints