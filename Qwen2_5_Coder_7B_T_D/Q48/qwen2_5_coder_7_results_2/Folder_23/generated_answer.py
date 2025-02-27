def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[36]
    total_sum = sum(range(a + 1, b)) - sum((nums[i] for i in range(21, 36)))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()