def return_binary_or_hexa(nums):
    if len(nums) < 44:
        return ''
    a = nums[37]
    b = nums[43]
    present = set(nums[37:44])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()