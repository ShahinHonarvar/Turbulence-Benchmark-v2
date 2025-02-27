def lists_with_product_equal_n(circular_list):

    def product_of_elements(elements):
        product = 1
        for element in elements:
            product *= element
        return product
    n = 990
    results = []
    size = len(circular_list)
    for start in range(size):
        for length in range(1, size + 1):
            if length > size:
                break
            sublist = [circular_list[(start + i) % size] for i in range(length)]
            if product_of_elements(sublist) == n:
                results.append(sublist)
    return results