def return_binary_or_hexa(nums):
    a, _, _, b = nums[:4]
    s = sum((x for x in range(a + 1, b) if x not in nums))
    if s == 0:
        return ''
    elif s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]