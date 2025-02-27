def lists_with_product_equal_n(circular_list):
    target_product = -82
    n = len(circular_list)
    found_sublists = []
    for i in range(n):
        for size in range(1, n + 1):
            temp_product = 1
            contiguous_list = circular_list[i:i + size]
            if len(contiguous_list) == size:
                for num in contiguous_list:
                    temp_product *= num
                if temp_product == target_product:
                    found_sublists.append(contiguous_list)
    return found_sublists