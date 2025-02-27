def return_binary_or_hexa(nums):
    a = nums[19]
    b = nums[32]
    total = sum(range(a + 1, b))
    not_present = [num for num in range(a + 1, b) if num not in nums[19:33]]
    total -= sum(not_present)
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]