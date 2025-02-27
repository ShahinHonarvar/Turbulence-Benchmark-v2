def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[9])
    expected_elements = set(range(a + 1, b))
    actual_elements = set(nums[1:9])
    missing_elements = expected_elements - actual_elements
    sum_of_missing_elements = sum(missing_elements)
    if sum_of_missing_elements % 2 == 1:
        result = bin(sum_of_missing_elements)[2:]
    else:
        result = hex(sum_of_missing_elements)[2:]
    return result