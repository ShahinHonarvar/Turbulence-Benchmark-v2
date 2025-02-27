def return_binary_or_hexa(nums):
    a, b = (nums[44], nums[78])
    s = set(nums[44:79])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total % 2:
        return bin(total)[2:]
    elif total:
        return hex(total)[2:]
    return ''