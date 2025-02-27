def lists_with_product_equal_n(circular_list):
    target_product = 537
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = circular_list[start:] + circular_list[:end]
            if len(sublist) <= n and product(sublist) == target_product:
                result.append(sublist)
    return result

def product(numbers):
    p = 1
    for number in numbers:
        p *= number
    return p