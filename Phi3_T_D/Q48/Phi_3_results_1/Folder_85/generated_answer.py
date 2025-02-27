def return_binary_or_hexa(nums):
    a, b = (nums[1], nums[8])
    missing_sum = sum(set(range(a + 1, b)) - set(nums[1:9]))
    if missing_sum % 2 == 0:
        hexa = hex(missing_sum)[2:]
        return hexa.upper()
    else:
        binary = bin(missing_sum)[2:]
        return binary