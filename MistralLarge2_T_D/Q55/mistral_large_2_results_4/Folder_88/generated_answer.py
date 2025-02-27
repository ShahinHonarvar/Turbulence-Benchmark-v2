def lists_with_product_equal_n(circular_list):

    def extend_circular_list(lst):
        return lst + lst

    def find_sublists_with_product(lst, product):
        sublists = []
        extended_list = extend_circular_list(lst)
        n = len(lst)
        for start in range(n):
            current_product = 1
            for end in range(start, start + n):
                current_product *= extended_list[end]
                if current_product == product:
                    sublists.append(extended_list[start:end + 1])
        return sublists
    return find_sublists_with_product(circular_list, -56)