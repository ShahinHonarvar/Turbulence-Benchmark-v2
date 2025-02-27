def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[35]
    sum_missing = sum(set(range(a + 1, b)).difference(nums[13:36]))
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:]