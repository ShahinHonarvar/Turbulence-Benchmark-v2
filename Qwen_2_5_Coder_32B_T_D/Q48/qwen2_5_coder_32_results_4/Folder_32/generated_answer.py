def return_binary_or_hexa(nums):
    a, b = (nums[86], nums[90])
    s = set(nums[87:90])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total % 2:
        return bin(total)[2:]
    elif total:
        return hex(total)[2:]
    return ''