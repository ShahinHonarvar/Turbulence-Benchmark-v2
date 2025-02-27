def lists_with_product_equal_n(circular_list):

    def find_sublists_with_product(start, target):
        product = 1
        current_sublist = []
        for end in range(start, start + len(circular_list)):
            index = end % len(circular_list)
            current_sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == target:
                result.append(list(current_sublist))
            elif abs(product) > abs(target) or circular_list[index] == 0:
                while current_sublist and (abs(product) > abs(target) or circular_list[index] == 0):
                    product //= current_sublist.pop(0)
                    if product == target:
                        result.append(list(current_sublist))
    result = []
    for start in range(len(circular_list)):
        find_sublists_with_product(start, -91)
    return result