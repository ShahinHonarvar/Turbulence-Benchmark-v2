def return_binary_or_hexa(nums):
    a = nums[33]
    b = nums[78]
    total = sum(range(a + 1, b)) - sum((num for num in nums if a + 1 <= num <= b - 1))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()