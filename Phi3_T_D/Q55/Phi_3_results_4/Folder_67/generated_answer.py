def lists_with_product_equal_n(circular_list, n=33):

    def get_sublists(start, end):
        result = []
        for i in range(start, end + 1):
            for j in range(i + 1, end + 1):
                sublist = circular_list[i:j]
                sublist += circular_list[:i] if i > 0 else []
                product = 1
                for num in sublist:
                    product *= num
                if product == n:
                    result.append(sublist)
        return result
    n = len(circular_list)
    return get_sublists(0, n) + get_sublists(1, n)