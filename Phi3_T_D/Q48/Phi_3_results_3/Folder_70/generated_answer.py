def return_binary_or_hexa(nums):
    if len(nums) < 0 or nums[42] != a or nums[69] != b:
        return 'Tuple indices are out of range or not as expected'
    missing_sum = (b - a - 1) * (a + b) // 2 - sum(nums[a + 1:b])
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]