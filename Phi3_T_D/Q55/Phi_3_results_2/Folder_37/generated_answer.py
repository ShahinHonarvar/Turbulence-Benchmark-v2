def lists_with_product_equal_n(circular_list):
    N = -76
    results = []
    list_length = len(circular_list)

    def check_product(start, end, product=1):
        current_product = product
        temp_results = []
        for i in range(start, end):
            current_product *= circular_list[i % list_length]
            if current_product == N:
                temp_results.append(circular_list[i % list_length:i % list_length + (i - start + 1)])
        return temp_results
    for i in range(list_length):
        temp_results = check_product(i, list_length) + check_product(0, i)
        results.extend(temp_results)
    return results