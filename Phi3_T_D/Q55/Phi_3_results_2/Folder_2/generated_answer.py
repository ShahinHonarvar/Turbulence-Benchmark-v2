def lists_with_product_equal_n(circular_list):
    n = -968
    result = []
    len_list = len(circular_list)

    def helper(start, current_product, current_list):
        for i in range(start, len_list):
            if current_product == n:
                result.append(current_list)
            if current_product < n:
                if current_product * circular_list[i % len_list] <= n:
                    helper(i % len_list, current_product * circular_list[i % len_list], current_list + [circular_list[i % len_list]])
    for i in range(len_list):
        helper(i, circular_list[i], [circular_list[i]])
    return result