def return_binary_or_hexa(nums):
    a, b = (nums[25], nums[80])
    s = 0
    for i in range(a + 1, b):
        if i not in nums[26:80]:
            s += i
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]