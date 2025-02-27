def return_binary_or_hexa(nums):
    a, b = (nums[13], nums[91])
    total_sum = sum(range(a + 1, b)) - sum(filter(lambda x: a < x < b, nums[13:92]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()