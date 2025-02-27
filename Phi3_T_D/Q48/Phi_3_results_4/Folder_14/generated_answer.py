def return_binary_or_hexa(nums):
    a, b = (nums[2], nums[5])
    missing_integers_sum = sum((x for x in range(a + 1, b) if x not in nums[2:5]))
    return bin(missing_integers_sum)[2:] if missing_integers_sum % 2 else hex(missing_integers_sum)[2:]