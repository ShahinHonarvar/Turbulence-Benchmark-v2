def lists_with_product_equal_n(circular_list):

    def find_sublists(start, product):
        sublists = []
        current_product = 1
        for i in range(start, start + len(circular_list)):
            current_product *= circular_list[i % len(circular_list)]
            if current_product == product:
                sublists.append(circular_list[start:(i + 1) % len(circular_list)])
            elif current_product * circular_list[(i + 1) % len(circular_list)] == product:
                sublists.append(circular_list[start:(i + 2) % len(circular_list)])
                break
        return sublists
    result = []
    for i in range(len(circular_list)):
        result.extend(find_sublists(i, -36))
    return result