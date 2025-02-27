def lists_with_product_equal_n(circular_list):

    def find_sublists(lst, target):
        n = len(lst)
        result = []
        for i in range(n):
            product = 1
            for j in range(n):
                product *= lst[(i + j) % n]
                if product == target:
                    result.append(lst[i:i + j + 1])
                if product == 0:
                    break
        return result
    return find_sublists(circular_list, -87)