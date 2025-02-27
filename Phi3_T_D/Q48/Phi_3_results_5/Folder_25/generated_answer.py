def return_binary_or_hexa(nums):
    a = nums[37]
    b = nums[43]
    absent_sum = sum((x for x in range(a + 1, b) if x not in nums[37:44]))
    if absent_sum % 2 == 0:
        return hex(absent_sum)[2:].upper()
    else:
        return bin(absent_sum)[2:]