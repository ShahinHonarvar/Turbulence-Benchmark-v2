def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[35]
    s = 0
    for i in range(a + 1, b):
        if i not in nums[21:35]:
            s += i
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()