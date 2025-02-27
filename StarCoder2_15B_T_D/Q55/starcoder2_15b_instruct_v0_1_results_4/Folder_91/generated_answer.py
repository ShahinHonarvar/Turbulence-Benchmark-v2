def lists_with_product_equal_n(list_of_ints):

    def helper(list_of_ints, sublist, product, index, n):
        if product == n:
            return [sublist]
        elif product > n or index >= len(list_of_ints):
            return []
        else:
            return helper(list_of_ints, sublist + [list_of_ints[index]], product * list_of_ints[index], index + 1, n) + helper(list_of_ints, sublist, product, index + 1, n)
    return helper(list_of_ints + list_of_ints, [], 1, 0, 2)