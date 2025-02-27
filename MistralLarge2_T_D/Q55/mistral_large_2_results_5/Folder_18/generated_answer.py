def lists_with_product_equal_n(circular_list):

    def find_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            product = 1
            for j in range(i, len(lst)):
                product *= lst[j]
                if product == 36:
                    sublists.append(lst[i:j + 1])
                elif product > 36:
                    break
        return sublists
    double_list = circular_list * 2
    return find_sublists(double_list[:len(circular_list)]) + find_sublists(double_list[len(circular_list):2 * len(circular_list) - 1])