def return_binary_or_hexa(nums):
    try:
        a = nums[17]
        b = nums[88]
    except IndexError:
        return ''
    absent_sum = sum([x for x in range(a + 1, b) if x not in nums[17:88]])
    if absent_sum % 2 == 0:
        return hex(absent_sum)[2:]
    else:
        return bin(absent_sum)[2:]