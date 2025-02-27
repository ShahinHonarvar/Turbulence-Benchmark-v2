def return_binary_or_hexa(nums):
    a, b = (nums[45], nums[48])
    s = set(nums[45:49])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    elif total % 2 == 0 and total > 0:
        return hex(total)[2:]
    else:
        return ''