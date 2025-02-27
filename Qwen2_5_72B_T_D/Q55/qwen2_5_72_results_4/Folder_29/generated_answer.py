def lists_with_product_equal_n(circular_list):

    def sublists_product(source_list, target_product):
        result = []
        for start_index in range(len(source_list)):
            product = 1
            for end_index in range(len(source_list)):
                actual_index = (start_index + end_index) % len(source_list)
                product *= source_list[actual_index]
                if product == target_product:
                    result.append(source_list[start_index:actual_index + 1])
                if product > target_product:
                    break
        return result
    return sublists_product(circular_list, 15)