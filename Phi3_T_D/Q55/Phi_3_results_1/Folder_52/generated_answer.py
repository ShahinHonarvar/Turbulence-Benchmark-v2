def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = 37
    result = []
    for size in range(1, n + 1):
        for start_index in range(n):
            end_index = (start_index + size - 1) % n
            if circular_list[start_index] == circular_list[end_index]:
                sublist = circular_list[start_index:end_index + 1]
                if n > size > 1 and product(sublist) == target_product:
                    result.append(sublist)
    return result

def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod