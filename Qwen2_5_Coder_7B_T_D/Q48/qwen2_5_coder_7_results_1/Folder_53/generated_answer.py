def return_binary_or_hexa(nums):
    a = nums[200]
    b = nums[202]
    total = sum(range(a + 1, b)) - sum((nums[i] for i in range(201, 202)))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()