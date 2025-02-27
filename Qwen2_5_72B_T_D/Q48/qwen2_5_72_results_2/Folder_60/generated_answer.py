def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[52]
    sum_missing = sum(set(range(a + 1, b)) - set(nums[39:52]))
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]

def check_function():
    test_tuple = tuple(range(100))
    result = return_binary_or_hexa(test_tuple)
    print(result)