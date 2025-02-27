def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[97]
    s = 0
    num_set = set(nums[11:97])
    for i in range(a + 1, b):
        if i not in num_set:
            s += i
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    return hex(s)[2:]