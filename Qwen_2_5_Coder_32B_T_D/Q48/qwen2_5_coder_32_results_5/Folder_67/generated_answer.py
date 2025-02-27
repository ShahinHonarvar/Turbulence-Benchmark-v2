def return_binary_or_hexa(nums):
    a = nums[44]
    b = nums[67]
    expected_sum = (b - 1 + a + 1) * (b - a - 1) // 2
    actual_sum = sum(nums[45:67])
    missing_sum = expected_sum - actual_sum
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:].upper()