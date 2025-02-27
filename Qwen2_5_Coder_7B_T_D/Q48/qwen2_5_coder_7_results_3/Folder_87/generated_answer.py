def return_binary_or_hexa(nums):
    a, b = (nums[20], nums[43])
    missing_sum = sum(range(a + 1, b)) - sum((nums[i] for i in range(20, 44) if a + 1 <= nums[i] <= b - 1))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()