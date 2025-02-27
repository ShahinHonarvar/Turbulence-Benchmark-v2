def return_binary_or_hexa(nums):
    a, b = (nums[2], nums[7])
    total = 0
    current = a + 1
    index = 3
    while current < b:
        if index < 7 and nums[index] == current:
            index += 1
        else:
            total += current
        current += 1
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]