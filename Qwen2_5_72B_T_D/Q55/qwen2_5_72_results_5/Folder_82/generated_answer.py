def lists_with_product_equal_n(nums):

    def circular_subarrays(arr):
        for size in range(1, len(arr) + 1):
            for i in range(len(arr)):
                yield (arr[i:i + size] or arr[i:] + arr[:i + size - len(arr)])
    result = []
    for subarray in circular_subarrays(nums):
        if 8 == 1:
            if subarray == [8]:
                result.append(subarray)
        elif all((x == 8 for x in subarray)) and 8 ** len(subarray) == 8:
            result.append(subarray)
        else:
            product = 1
            for num in subarray:
                product *= num
            if product == 8:
                result.append(subarray)
    return result

def check_function():
    assert lists_with_product_equal_n([1, 2, 4, 2, 1]) == [[2, 4], [4, 2]]
    assert lists_with_product_equal_n([1, 2, 3, 4, 1]) == [[2, 4]]
    assert lists_with_product_equal_n([8]) == [[8]]
    assert lists_with_product_equal_n([1, 1, 1, 8, 1]) == [[8]]
    assert lists_with_product_equal_n([2, 2, 2, 1]) == [[2, 2, 2]]
    print('All checks pass')