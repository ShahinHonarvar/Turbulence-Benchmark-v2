def lists_with_product_equal_n(circular_list):
    n = -61
    results = []
    size = len(circular_list)
    for i in range(size):
        for j in range(i, size):
            current_list = circular_list[i:j + 1]
            if current_list:
                product = 1
                for number in current_list:
                    product *= number
                if product == n:
                    results.append(current_list)
    for result in results:
        if result not in results[:results.index(result)]:
            yield result