def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[10]
    existing_set = set(nums[1:10])
    total_sum = sum((i for i in range(a + 1, b) if i not in existing_set))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]