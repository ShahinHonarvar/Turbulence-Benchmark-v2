def return_binary_or_hexa(nums):
    a = nums[90]
    b = nums[200]
    total_sum = sum(range(a + 1, b)) - sum((x for x in nums if a < x < b))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()