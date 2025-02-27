def return_binary_or_hexa(nums):
    start, end = (nums[25] + 1, nums[80] - 1)
    missing_sum = sum((i for i in range(start, end + 1) if i not in nums[25:80]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()