def return_binary_or_hexa(nums):
    a_index, b_index = (20, 35)
    a, b = (nums[a_index], nums[b_index])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[a_index + 1:b_index]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]