def return_binary_or_hexa(nums):
    if not nums or len(nums) < 201:
        return ''
    a = nums[80]
    b = nums[200]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in nums:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]