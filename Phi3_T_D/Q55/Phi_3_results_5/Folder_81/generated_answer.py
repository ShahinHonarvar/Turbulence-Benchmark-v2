def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    product_target = -8
    result = []

    def generate_sublists(start, temp_list, tmp_product):
        if tmp_product == product_target:
            result.append(temp_list)
            return
        if start == size:
            return
        for i in range(size):
            new_start = (start + i) % size
            new_list = temp_list + [circular_list[new_start]]
            new_product = tmp_product * circular_list[new_start]
            if new_product == product_target:
                result.append(new_list)
            elif new_product < product_target:
                generate_sublists(new_start, new_list, new_product)
    generate_sublists(0, [], 1)
    return result