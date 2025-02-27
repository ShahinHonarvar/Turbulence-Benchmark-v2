def lists_with_product_equal_n(circular_list, n):

    def get_sublists(list_, product):
        sublists = []
        for i in range(len(list_)):
            sublist = []
            current_product = 1
            for j in range(i, len(list_)):
                sublist.append(list_[j])
                current_product *= list_[j]
                if current_product == product:
                    sublists.append(sublist)
                elif current_product > product:
                    break
        return sublists
    sublists = get_sublists(circular_list, n)
    if not sublists:
        return []
    circular_sublists = []
    for sublist in sublists:
        circular_sublists.extend([sublist[i:] + sublist[:i] for i in range(len(sublist))])
    return circular_sublists