def return_binary_or_hexa(nums):
    a, b = (nums[1], nums[8])
    missing_sum = sum(set(range(a + 1, b)) - set(nums[2:8]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:].upper()

def check_solution():
    example1 = (1, 3, 4, 5, 6, 7, 8, 9, 11)
    example2 = (0, 2, 3, 4, 5, 6, 7, 8, 10)
    assert return_binary_or_hexa(example1) == '10011', 'Example 1 is incorrect'
    assert return_binary_or_hexa(example2) == '9', 'Example 2 is incorrect'
    print('All examples are correct!')