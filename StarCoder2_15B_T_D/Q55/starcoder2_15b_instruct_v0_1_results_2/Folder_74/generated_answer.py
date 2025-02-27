def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i):
            sublist = circular_list[i:j]
            if len(sublist) > len(circular_list):
                break
            product = 1
            for num in sublist:
                product *= num
            if product == 51:
                yield sublist