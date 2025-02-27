def return_binary_or_hexa(nums):
    a = nums[3]
    b = nums[9]
    total_sum = sum(range(a + 1, b)) - sum((x for x in nums if a < x < b))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]