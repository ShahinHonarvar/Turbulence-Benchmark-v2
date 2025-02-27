def lists_with_product_equal_n(circular_list):

    def find_sublists_product(start, end, product=1):
        if start == end and product != -20:
            return []
        if start == len(circular_list) and product == -20:
            return [circular_list[start:end + 1]]
        res = find_sublists_product(start, end + 1, product * circular_list[end])
        if start > 0:
            res += find_sublists_product(start - 1, end, product // circular_list[start - 1])
        return res
    return find_sublists_product(0, 0)