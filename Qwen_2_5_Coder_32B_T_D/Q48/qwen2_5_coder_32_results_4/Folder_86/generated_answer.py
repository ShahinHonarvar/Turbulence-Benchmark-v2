def return_binary_or_hexa(nums):
    a = nums[19]
    b = nums[32]
    s = 0
    current = a + 1
    idx = 20
    while current < b:
        if idx < 32 and nums[idx] == current:
            idx += 1
        else:
            s += current
        current += 1
    if s == 0:
        return ''
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:]