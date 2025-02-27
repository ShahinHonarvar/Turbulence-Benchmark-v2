def lists_with_product_equal_n(lst):

    def find_sublists_with_product(product, start, end):
        sublists = []
        current_product = 1
        current_sublist = []
        for i in range(start, end):
            current_product *= lst[i % len(lst)]
            current_sublist.append(lst[i % len(lst)])
            if current_product == product:
                sublists.append(current_sublist[:])
            elif current_product > product:
                while current_sublist and current_product > product:
                    current_product //= current_sublist.pop(0)
                if current_product == product:
                    sublists.append(current_sublist[:])
        return sublists
    result = set()
    for i in range(len(lst)):
        result.update(find_sublists_with_product(632, i, i + len(lst)))
    return [list(sublist) for sublist in result]