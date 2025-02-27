def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[2])
    total = sum(range(a + 1, b))
    missing_nums = [num for num in range(a + 1, b) if num not in nums]
    for num in missing_nums:
        total -= num
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()