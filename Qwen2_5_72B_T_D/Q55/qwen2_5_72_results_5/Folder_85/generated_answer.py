def lists_with_product_equal_n(nums):
    target_product = -97
    n = len(nums)
    result = []

    def circular_product_sublists(start, length, product):
        if product == target_product:
            result.append(nums[start:start + length])
        if product != 0 and abs(target_product / product) > n:
            return
        for size in range(1, n + 1):
            current_product = product
            for i in range(length):
                index = (start + i) % n
                current_product *= nums[index]
            if current_product == target_product:
                result.append(nums[start:start + size])
    for i in range(n):
        circular_product_sublists(i, 1, nums[i])
    return result

def check_function():
    test_cases = [([1, 2, -97, 3, 1, 2, 1], [[-97]]), ([1, 1, 1, 1, -97], [[-97]]), ([1, 2, 3, 4, 5], []), ([3, 32, -3, 3, -1, -97, 3], [[-97]])]
    for nums, expected in test_cases:
        result = lists_with_product_equal_n(nums)
        assert len(result) == len(expected), f'Failed for {nums}, expected {expected}, got {result}'
        for elem in expected:
            assert elem in result, f'Failed for {nums}, expected {expected}, got {result}'
    print('All test cases passed.')