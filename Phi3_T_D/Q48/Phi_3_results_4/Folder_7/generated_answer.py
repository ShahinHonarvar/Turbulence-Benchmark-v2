def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[97]
    absent_sum = sum((x for x in range(a + 1, b) if x not in nums[10:97]))
    if absent_sum % 2 == 0:
        return hex(absent_sum)[2:]
    else:
        return bin(absent_sum)[2:]