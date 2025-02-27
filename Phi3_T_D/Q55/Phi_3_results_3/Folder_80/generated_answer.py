def lists_with_product_equal_n(circular_list):
    n = 43
    num_elements = len(circular_list)
    product_list = []

    def generate_sublists(index, current_product, current_sublist):
        nonlocal product_list
        if index == num_elements:
            if current_product == n:
                product_list.append(current_sublist)
            return
        generate_sublists(index + 1, current_product * circular_list[index], current_sublist + [circular_list[index]])
        generate_sublists(index + 1, current_product, current_sublist)
    generate_sublists(0, 1, [])
    return product_list