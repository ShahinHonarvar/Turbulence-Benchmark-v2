def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[81]
    present = set(nums[39:81])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]