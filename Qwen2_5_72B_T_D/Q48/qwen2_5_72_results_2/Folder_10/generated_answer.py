def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[54]
    existing_nums = set(nums[37:54])
    missing_sum = sum((num for num in range(a + 1, b) if num not in existing_nums))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]