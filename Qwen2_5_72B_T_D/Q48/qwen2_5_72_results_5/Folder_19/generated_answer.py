def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[4]
    s = sum(set(range(a + 1, b)) - set(nums[2:4]))
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]