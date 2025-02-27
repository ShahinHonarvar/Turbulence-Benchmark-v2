def return_binary_or_hexa(nums):
    if not nums or len(nums) < 86 or len(nums) > 86 or (nums[36] >= nums[85]):
        return ''
    a = nums[36]
    b = nums[85]
    available_nums = set(nums[37:85])
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in available_nums:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]