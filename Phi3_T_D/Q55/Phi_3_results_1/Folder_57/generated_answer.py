def lists_with_product_equal_n(circular_list, target=75):
    n = len(circular_list)
    sublists = []

    def product_of_elements(sublist):
        product = 1
        for item in sublist:
            product *= item
        return product
    for i in range(n):
        for length in range(1, n + 1):
            if length > n:
                break
            sublist = circular_list[i:i + length] + circular_list[:length - (n - i)]
            if product_of_elements(sublist) == target:
                sublists.append(sublist)
    return sublists