def return_binary_or_hexa(nums):
    a = nums[7]
    b = nums[9]
    total_sum = sum(range(a + 1, b)) - sum(set(nums[7:9]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()