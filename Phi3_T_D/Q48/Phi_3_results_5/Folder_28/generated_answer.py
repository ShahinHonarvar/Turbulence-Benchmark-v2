def return_binary_or_hexa(nums):
    a = nums[86] + 1
    b = nums[99] - 1
    expected_sum = sum(range(a, b + 1))
    present_sum = sum((i for i in range(a, b + 1) if a <= i <= b and i in nums[86:99]))
    missing_sum = expected_sum - present_sum
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]