def lists_with_product_equal_n(circular_list):

    def get_sublists_with_product(input_list, target_product):
        result = []
        for start in range(len(input_list)):
            product = 1
            for end in range(len(input_list)):
                index = (start + end) % len(input_list)
                product *= input_list[index]
                if product == target_product:
                    result.append(input_list[start:index + 1])
        return result
    return get_sublists_with_product(circular_list, 53)