def return_binary_or_hexa(nums):
    missing_sum = sum(range(nums[18] + 1, nums[52])) - sum(nums[18:52])
    return bin(missing_sum).replace('0b', '').lstrip('0') if missing_sum % 2 else hex(missing_sum).replace('0x', '').upper() if missing_sum >= 16 else hex(missing_sum).replace('0x', '').lower()