def lists_with_product_equal_n(circular_list, n=-83):

    def find_sublists(lst):
        sublists = []
        for start in range(len(lst)):
            product = 1
            for end in range(start, len(lst)):
                product *= lst[end]
                if product == n:
                    sublists.append(lst[start:end + 1])
                elif product > n:
                    break
        return sublists
    circular_list += circular_list
    return find_sublists(circular_list[:len(circular_list) // 2]) + find_sublists(circular_list[len(circular_list) // 2:])