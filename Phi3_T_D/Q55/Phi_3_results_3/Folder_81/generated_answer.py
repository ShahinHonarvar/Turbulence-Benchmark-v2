from itertools import cycle

def lists_with_product_equal_n(circular_list):

    def product_of_elements(sublist):
        product = 1
        for item in sublist:
            product *= item
        return product

    def find_sublists(lst):
        length = len(lst)
        sublists = []
        for start in range(length):
            for end in range(start, length):
                if lst[end] == lst[0] and end - start == length - 1:
                    end += 1
                sub = lst[start:end + 1]
                if product_of_elements(sub) == n:
                    sublists.append(sub)
        return sublists
    n = -8
    circular_cycle = cycle(circular_list)
    initial_list = list((next(circular_cycle) for _ in range(len(circular_list))))
    found_sublists = find_sublists(initial_list)
    extended_list = initial_list + [initial_list[0]]
    found_sublists.update(find_sublists(extended_list))
    return found_sublists