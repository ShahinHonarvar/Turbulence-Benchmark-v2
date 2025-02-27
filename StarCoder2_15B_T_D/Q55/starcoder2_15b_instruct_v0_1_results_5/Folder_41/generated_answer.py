def lists_with_product_equal_n(circular_list, n):
    result = []

    def find_sublists_with_product(current_list, current_product, start_index):
        for i in range(start_index, len(current_list)):
            if current_product * current_list[i] == n:
                result.append(current_list[start_index:i + 1])
            elif current_product * current_list[i] < n:
                find_sublists_with_product(current_list, current_product * current_list[i], i + 1)
    find_sublists_with_product(circular_list + circular_list, 1, 0)
    return result