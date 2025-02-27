def lists_with_product_equal_n(circular_list):
    result = []
    n = 25
    min_size = 2
    max_size = len(circular_list)
    for size in range(min_size, max_size + 1):
        for start in range(0, len(circular_list)):
            end = (start + size) % len(circular_list)
            if all((item == 5 or item == 1 for item in circular_list[start:end])):
                product = 1
                for num in circular_list[start:end]:
                    product *= num
                if product == n:
                    result.append(circular_list[start:end])
    return result