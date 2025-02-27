def return_binary_or_hexa(nums):
    a = nums[77]
    b = nums[84]
    num_set = set(nums[77:84])
    sum_val = sum((num for num in range(a + 1, b) if num not in num_set))
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()