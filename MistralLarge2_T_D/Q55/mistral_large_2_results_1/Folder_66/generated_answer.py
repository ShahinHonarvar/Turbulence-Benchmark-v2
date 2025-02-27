def lists_with_product_equal_n(circular_list):
    n = 78

    def get_sublist_products(lst):
        length = len(lst)
        sublist_products = []
        for i in range(length):
            product = 1
            for j in range(length):
                product *= lst[(i + j) % length]
                if product == n:
                    sublist_products.append(lst[i:i + j + 1])
                elif product > n:
                    break
        return sublist_products
    return get_sublist_products(circular_list)