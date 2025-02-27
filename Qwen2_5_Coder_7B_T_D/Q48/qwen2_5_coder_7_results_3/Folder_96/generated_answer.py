def return_binary_or_hexa(nums):
    a = nums[50]
    b = nums[200]
    total = sum(range(a + 1, b))
    if any((num in nums[51:200] for num in range(a + 1, b))):
        return ''
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()