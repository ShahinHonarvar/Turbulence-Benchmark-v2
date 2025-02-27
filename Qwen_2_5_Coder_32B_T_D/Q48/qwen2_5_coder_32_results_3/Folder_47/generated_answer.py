def return_binary_or_hexa(nums):
    a = nums[29]
    b = nums[53]
    s = 0
    num_set = set(nums[30:53])
    for i in range(a + 1, b):
        if i not in num_set:
            s += i
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()