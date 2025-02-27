def return_binary_or_hexa(nums):
    a = nums[51]
    b = nums[76]
    total_sum = sum(range(a + 1, b)) - sum(filter(lambda x: x > a and x < b, nums[51:77]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()