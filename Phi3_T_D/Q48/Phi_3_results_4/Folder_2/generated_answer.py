def return_binary_or_hexa(nums):
    a = nums[72]
    b = nums[93]
    absent_sum = sum(set(range(a + 1, b)).difference(nums[72:94]))
    if absent_sum % 2 != 0:
        return bin(absent_sum)[2:]
    else:
        return hex(absent_sum)[2:]