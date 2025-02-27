def lists_with_product_equal_n(circular_list, n=-7):
    results = []
    num_items = len(circular_list)
    circular_list = circular_list + circular_list[:-1]
    for start in range(num_items):
        product = 1
        for end in range(start, num_items * 2):
            product *= circular_list[end % num_items]
            if product == n and len(results) == 0 or len(results[-1]) != end - start:
                results.append(circular_list[start:min(start + end, num_items)])
            if product > n:
                break
    return results