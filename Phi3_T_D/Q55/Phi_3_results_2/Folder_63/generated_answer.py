def circular_product_check(arr, start, n, target):
    if start >= len(arr):
        start = 0
    product = 1
    for i in range(n):
        product *= arr[start]
        if product > target:
            return False
        start = (start + 1) % len(arr)
    return product == target

def lists_with_product_equal_n(circle_list):
    results = []
    n = len(circle_list)
    target_product = 96
    for size in range(1, n + 1):
        for start in range(n):
            if circular_product_check(circle_list, start, size, target_product):
                results.append(circle_list[start:start + size])
    return results