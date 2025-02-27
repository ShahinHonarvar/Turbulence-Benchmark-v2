def lists_with_product_equal_n(circular_list):

    def find_sublists(start, target, seen=None):
        if seen is None:
            seen = []
        if start == len(circular_list):
            return []
        product = 1
        sublist = []
        for i in range(start, len(circular_list)):
            if circular_list[i] in seen:
                continue
            product *= circular_list[i]
            sublist.append(circular_list[i])
            if product == target:
                left_sublists = find_sublists(0, target, sublist)
                right_sublists = find_sublists(i + 1, target, [x for x in seen if x != circular_list[i]])
                return [sublist] + left_sublists + right_sublists
            seen.append(circular_list[i])
        return []
    return find_sublists(0, -9, [])