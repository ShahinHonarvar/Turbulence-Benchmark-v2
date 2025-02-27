def return_binary_or_hexa(nums):
    a, b = (nums[86], nums[99])
    s = sum((x for x in range(a + 1, b) if x not in nums[87:99]))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]