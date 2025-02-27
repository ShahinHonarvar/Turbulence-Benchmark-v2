def lists_with_product_equal_n(circular_list):

    def find_sublists(head, tail, target, current=1, sublist=[]):
        if tail == head:
            if current * sublist[0] == target:
                return [sublist]
            return []
        sublists = []
        for i in range(tail if tail < head else tail + 1, len(circular_list) + tail if tail < head else len(circular_list) + 1):
            sublist.append(circular_list[i % len(circular_list)])
            next_sublists = find_sublists(head, i, target, current * circular_list[i % len(circular_list)], sublist)
            sublists.extend(next_sublists)
            sublist.pop()
        return sublists
    n = 85
    sublists = find_sublists(-1, 0, n)
    return sublists