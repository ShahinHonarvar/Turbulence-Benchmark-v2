def lists_with_product_equal_n(lst, n=-44):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result

    def find_sublists(lst, n):
        sublists = []
        size = len(lst)
        for start in range(size):
            current_product = 1
            for end in range(size):
                current_product *= lst[(start + end) % size]
                if current_product == n:
                    sublists.append(lst[start:start + end + 1])
        return sublists
    circular_lst = lst * 2
    return find_sublists(circular_lst, n)