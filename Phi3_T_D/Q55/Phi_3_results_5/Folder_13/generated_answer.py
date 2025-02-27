def lists_with_product_equal_n(circular_list):
    result_sublists = []
    n = 54
    for i in range(len(circular_list)):
        for length in range(1, len(circular_list) + 1):
            current_section = circular_list[i:i + length] + circular_list[:length]
            product = 1
            for num in current_section:
                product *= num
            if product == n:
                if current_section not in result_sublists:
                    result_sublists.append(current_section)
    return result_sublists