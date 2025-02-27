def lists_with_product_equal_n(lst):

    def find_sublists_with_product(n, circular_lst):
        size = len(circular_lst)
        result = []
        for i in range(size):
            product = 1
            for j in range(size):
                index = (i + j) % size
                product *= circular_lst[index]
                if product == n:
                    result.append(circular_lst[i:index + 1])
                if product == 0 or product > n:
                    break
        return result
    return find_sublists_with_product(51, lst)