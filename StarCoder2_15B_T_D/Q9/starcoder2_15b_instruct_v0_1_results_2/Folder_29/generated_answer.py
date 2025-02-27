def all_odd_ints_inclusive(nums):
    result = []
    for i in range(len(nums)):
        if i >= 59 and i <= 97 and (nums[i] % 2 == 1):
            result.append(nums[i])
    return result