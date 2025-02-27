def lists_with_product_equal_n(circular_list, n=33):
    results = []
    for end in range(len(circular_list)):
        temp_product = 1
        temp_list = []
        for start in range(end, end + len(circular_list)):
            index = start % len(circular_list)
            value = circular_list[index]
            temp_product *= value
            temp_list.append(value)
            if temp_product == n:
                results.append(temp_list.copy())
            if temp_product > n:
                temp_product = 1
                temp_list = []
                break
    return results