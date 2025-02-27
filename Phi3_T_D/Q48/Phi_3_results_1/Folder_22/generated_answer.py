def return_binary_or_hexa(nums):
    a = nums[40]
    b = nums[200] if 200 < len(nums) else a - 1
    included_numbers = set(nums[40:200 + 1])
    summed_numbers = sum((i for i in range(a + 1, b) if i not in included_numbers))
    if summed_numbers % 2 == 0:
        return hex(summed_numbers)[2:]
    else:
        return bin(summed_numbers)[2:]