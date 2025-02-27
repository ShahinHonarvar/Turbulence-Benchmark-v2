def return_binary_or_hexa(nums):
    a = nums[110]
    b = nums[348]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[111:348]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_data = tuple(range(1000))
    result = return_binary_or_hexa(test_data)
    print(result)