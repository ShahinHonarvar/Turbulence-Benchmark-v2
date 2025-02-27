def lists_with_product_equal_n(circular_list):
    target_product = 15
    result = []
    list_size = len(circular_list)

    def find_sublists(start, product=1):
        if product == target_product:
            result.append(circular_list[start:start + len(found_factors)])
            return
        if start == list_size:
            return
        for end in range(start, list_size):
            current_product = 1
            found_factors = []
            for j in range(start, end + 1):
                current_product *= circular_list[j % list_size]
                if current_product > target_product:
                    break
                if current_product == target_product:
                    found_factors = circular_list[start:j + 1]
            if found_factors:
                result.append(found_factors)
            find_sublists(end + 1, product * circular_list[(end + 1) % list_size])
    find_sublists(0, circular_list[0])
    return result