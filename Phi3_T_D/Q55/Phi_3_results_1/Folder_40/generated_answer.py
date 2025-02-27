def circular_list_product_equal_n(lst, n=9):
    circular_length = len(lst)
    results = []
    for size in range(1, circular_length + 1):
        for start_idx in range(circular_length):
            end_idx = (start_idx + size) % circular_length
            if end_idx < start_idx:
                product = 1
                for i in range(start_idx, end_idx + 1):
                    product *= lst[i % circular_length]
                if product == -n:
                    results.append(lst[start_idx:end_idx + 1])
    return results

def lists_with_product_equal_n(circular):
    return circular_list_product_equal_n(circular)