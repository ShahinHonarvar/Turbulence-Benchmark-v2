def lists_with_product_equal_n(circular_list):
    n = -33
    result = []

    def search(sublist, start, product):
        nonlocal result
        for i in range(start, start + len(circular_list)):
            index = i % len(circular_list)
            new_product = product * circular_list[index]
            if new_product == n or (new_product > 0 and n / new_product).is_integer():
                result.append(circular_list[start:index + 1])
                search(circular_list, index + 1, 1)
                search(circular_list, start, new_product)
    search(circular_list, 0, 1)
    return result