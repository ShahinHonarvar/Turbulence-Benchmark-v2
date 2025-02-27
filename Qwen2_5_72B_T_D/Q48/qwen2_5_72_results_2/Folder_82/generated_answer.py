def return_binary_or_hexa(nums):
    if len(nums) < 201:
        return ''
    a, b = (nums[20], nums[200])
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in nums:
            missing_sum += i
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]