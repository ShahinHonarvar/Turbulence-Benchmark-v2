def return_binary_or_hexa(nums):
    a, b = (nums[70], nums[200])
    absent_sum = sum((x for x in range(a + 1, b) if x not in nums[70:200]))
    if absent_sum % 2 == 0:
        return hex(absent_sum).upper().lstrip('0').lstrip('X')
    else:
        return bin(absent_sum)[2:]