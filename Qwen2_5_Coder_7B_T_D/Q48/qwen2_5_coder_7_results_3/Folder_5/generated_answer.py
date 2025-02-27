def return_binary_or_hexa(nums):
    a = nums[2]
    b = nums[8]
    total = sum(range(a + 1, b))
    missing = set(range(a + 1, b)) - set(nums[3:8])
    subtracted = total - sum(missing)
    if subtracted % 2 == 1:
        return bin(subtracted)[2:]
    else:
        return hex(subtracted)[2:].upper()