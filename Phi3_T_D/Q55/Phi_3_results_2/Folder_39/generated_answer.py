def lists_with_product_equal_n(circular_list):
    product = -46
    results = []
    for length in range(1, len(circular_list) + 1):
        for start in range(len(circular_list)):
            sublist = circular_list[start:start + length]
            if len(sublist) == length and product == 1:
                result_product = 1
                for num in sublist:
                    result_product *= num
                if result_product == product:
                    results.append(sublist)
            if start > 0 and length + start >= len(circular_list):
                wrapped_sublist = circular_list[start:] + circular_list[:length + start - len(circular_list)]
                wrapped_product = 1
                for num in wrapped_sublist:
                    wrapped_product *= num
                if wrapped_product == product:
                    results.append(wrapped_sublist)
    return results