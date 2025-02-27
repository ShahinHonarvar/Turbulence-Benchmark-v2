def lists_with_product_equal_n(circular_list):
    target_product = -83
    result = []
    curr_product = 1
    for start in range(len(circular_list)):
        if curr_product == 0:
            curr_product = 1
            start += 1
            continue
        for end in range(start, len(circular_list) + start):
            next_val = circular_list[end % len(circular_list)]
            curr_product *= next_val
            if curr_product == target_product:
                result.append(circular_list[start:end % len(circular_list) + 1])
                curr_product = 1
                break
            if next_val != 0 and curr_product > target_product:
                curr_product = 1
                break
    return result